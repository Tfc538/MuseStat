"""
Language detection and language-specific processing.
"""

from __future__ import annotations
from ..core.text_processing import clean_markdown
from functools import lru_cache
import unicodedata
from typing import Iterable, Set

# Optional import for language detection
try:
    import langdetect
    LANG_DETECT_SUPPORT = True
except ImportError:
    LANG_DETECT_SUPPORT = False


def detect_language(text: str) -> str:
    """
    Detect the language of the text.
    
    Args:
        text: Text to analyze
        
    Returns:
        Language code (e.g., 'en', 'ko') or 'unknown' if detection fails
    """
    if not LANG_DETECT_SUPPORT:
        return "unknown"
    
    try:
        # Sample the text to avoid performance issues
        sample = clean_markdown(text)[:5000]
        lang = langdetect.detect(sample)
        return lang
    except Exception:
        return "unknown"


# --- Core stopword inventories (lowercased) ---
# NOTE: These are compact, high-signal sets aimed at fiction/non-technical text.
# You can extend them safely via the extra/exclude parameters.
_STOPWORDS: dict[str, frozenset[str]] = {
    # English
    "en": frozenset({
        "the","be","to","of","and","a","in","that","have","i","it","for","not","on","with","he","as",
        "you","do","at","this","but","his","by","from","they","we","say","her","she","or","an","will",
        "my","one","all","would","there","their","was","were","been","has","had","are","is","am","can",
        "could","did","does","doing","done","what","which","who","whom","when","where","why","how","up",
        "out","if","about","than","into","so","me","your","yours","our","ours","its","itself","themselves",
        "him","himself","hers","herself","them","these","those","this","that","here","there","because","over",
        "under","again","further","then","once","only","just","also","even","ever","never","very"
    }),
    # German
    "de": frozenset({
        "der","die","das","und","in","den","von","zu","mit","sich","des","im","auf","für","ist","dem",
        "nicht","ein","eine","als","auch","es","an","werden","aus","er","hat","dass","so","was","wir",
        "bei","oder","aber","wenn","noch","nur","schon","wie","man","am","nach","mehr","über","bis",
        "vor","durch","ohne","zwischen","sein","seine","seiner","ihr","ihre","ihrer","du","ich","ihr",
        "euch","uns","einer","einem","einen"
    }),
    # French
    "fr": frozenset({
        "le","la","les","de","des","du","un","une","et","en","dans","que","qui","pour","sur","pas",
        "plus","avec","ne","au","aux","se","ce","cet","cette","ces","il","elle","ils","elles","nous",
        "vous","on","par","comme","mais","ou","où","donc","ni","car","été","etre","être","avoir"
    }),
    # Spanish
    "es": frozenset({
        "el","la","los","las","de","del","un","una","unos","unas","y","en","que","por","con","para",
        "como","más","muy","no","sí","se","su","sus","al","lo","le","les","o","u","ya","entre","cuando",
        "donde","dónde","porque","sobre","también"
    }),
    # Italian
    "it": frozenset({
        "il","lo","la","i","gli","le","un","una","uno","di","a","da","in","con","su","per","tra","fra",
        "che","chi","come","quale","quanto","non","più","meno","sì","no","noi","voi","lui","lei","loro",
        "cui","anche","già","solo","ancora"
    }),
    # Portuguese (covers pt + pt-br)
    "pt": frozenset({
        "o","a","os","as","um","uma","uns","umas","de","do","da","dos","das","em","no","na","nos","nas",
        "e","que","por","com","para","como","mais","muito","não","sim","se","sua","seu","suas","seus",
        "ao","aos","à","às","já","entre","quando","onde","também"
    }),
    # Dutch
    "nl": frozenset({
        "de","het","een","en","van","op","te","dat","die","in","met","niet","voor","als","bij","om",
        "aan","je","jij","wij","we","zij","ze","hun","hen","maar","ook","al","nog"
    }),
    # Swedish
    "sv": frozenset({
        "och","det","att","i","en","jag","hon","som","han","på","den","med","var","sig","för","så",
        "till","är","var","de","inte","om","ett","men","här","där","har","ha","vi","ni","er","oss"
    }),
    # Danish
    "da": frozenset({
        "og","i","jeg","det","at","en","den","til","er","som","på","de","med","han","af","for","ikke",
        "der","var","mig","sig","men","et","har","om","vi","min","havde","hun","nu","over","da"
    }),
    # Norwegian (Bokmål-ish)
    "no": frozenset({
        "og","i","jeg","det","at","en","den","til","er","som","på","de","med","han","av","for","ikke",
        "der","var","meg","seg","men","et","har","om","vi","min","hadde","hun","nå","over","da"
    }),
    # Finnish
    "fi": frozenset({
        "ja","on","se","että","ei","kuin","oli","mutta","jos","mitä","kun","niin","kanssa","tai","vain",
        "myös","jo","muun","me","te","he","hän","ne","se","nämä","nämä","tuo","tämä"
    }),
    # Russian
    "ru": frozenset({
        "и","в","во","не","что","он","на","я","с","со","как","а","то","все","она","так","его","но",
        "да","ты","к","у","же","вы","за","бы","по","ее","мне","есть","они","только","мы","быть","был",
        "когда","еще","до","из","ему","теперь","при","ли","если","уже","или","ни","были"
    }),
    # Polish
    "pl": frozenset({
        "i","w","na","to","że","z","do","się","nie","jest","jak","ale","o","po","co","za","od","tak",
        "dla","tego","ten","ta","tam","tu","być","był","była","było","już"
    }),
    # Czech
    "cs": frozenset({
        "a","i","v","ve","na","že","se","si","je","já","ty","on","ona","ono","my","vy","oni","ale",
        "ne","co","jak","k","do","za","po","u","od","pro","bez","už"
    }),
    # Turkish
    "tr": frozenset({
        "ve","bir","bu","da","de","için","ile","ama","fakat","çok","az","daha","en","mi","mu","mü",
        "ne","niçin","neden","çünkü","gibi","kadar","ise","ya","ya da","veya","şu","o","bu","şöyle"
    }),
    # Greek
    "el": frozenset({
        "και","το","η","να","του","την","τι","σε","με","από","που","για","ως","πως","πολύ","ότι",
        "είναι","ή","θα","αν","δε","δεν","ενα","μια","στο","στη","στους","στις"
    }),
    # Arabic
    "ar": frozenset({
        "و","في","على","من","إلى","عن","أن","إن","كان","تكون","التي","الذي","هذا","هذه","ذلك",
        "تلك","ما","لا","لم","لن","مع","كل","كما","بعد","قبل","دون","حيث","قد","أي","أو"
    }),
    # Persian
    "fa": frozenset({
        "و","در","به","از","که","این","را","با","برای","آن","بود","است","می","تا","اما","یا",
        "نه","اگر","هم","همه","هیچ","چون","چرا","کجا","چه","کی"
    }),
    # Hebrew
    "he": frozenset({
        "של","על","עם","אל","אלו","אלה","זה","זאת","לא","כן","אם","או","כי","הוא","היא","הם",
        "הן","אני","אנחנו","אתה","את","אתם","אתן","גם","עוד","כמו","אבל"
    }),
    # Hindi
    "hi": frozenset({
        "और","के","का","की","को","पर","से","है","थे","था","यह","ये","वह","वे","एक","में",
        "तथा","जैसे","लिए","ताकि","किया","करना","हैं","या","भी"
    }),
    # Urdu
    "ur": frozenset({
        "اور","کے","کا","کی","کو","پر","سے","ہے","تھا","تھے","یہ","وہ","ایک","میں","لیے","جیسے",
        "بھی","یا","ہیں","تاکہ","کرنا","کیا"
    }),
    # Bengali
    "bn": frozenset({
        "এবং","এর","একটি","এই","ও","করে","করা","কী","কি","কে","সে","তা","তাই","না","হয়","হয়ে",
        "হলে","যে","যদি","যখন","যেখানে","আর","কেন","কোন","কোনও"
    }),
    # Indonesian
    "id": frozenset({
        "yang","dan","di","ke","dari","untuk","pada","dengan","tidak","ini","itu","adalah","atau",
        "sebagai","oleh","para","saja","karena","agar","kami","kita","mereka","ada","akan"
    }),
    # Malay
    "ms": frozenset({
        "yang","dan","di","ke","dari","untuk","pada","dengan","tidak","ini","itu","adalah","atau",
        "sebagai","oleh","para","saja","kerana","agar","kami","kita","mereka","ada","akan"
    }),
    # Vietnamese
    "vi": frozenset({
        "và","của","là","trong","một","những","các","được","cho","với","không","có","đã","đang",
        "từ","này","kia","đó","khi","ở","như","nhưng","hoặc"
    }),
    # Thai
    "th": frozenset({
        "และ","ของ","คือ","ใน","ที่","เป็น","ได้","ให้","ไม่","มี","หรือ","กับ","จาก","ว่า",
        "ซึ่ง","นี้","นั้น","ก็","ได้","แล้ว","เมื่อ","โดย"
    }),
    # Romanian
    "ro": frozenset({
        "și","în","pe","la","cu","de","din","un","o","este","sunt","nu","da","sau","care","că",
        "pentru","mai","foarte","cum","ce","când","unde","fără"
    }),
    # Hungarian
    "hu": frozenset({
        "és","a","az","hogy","nem","van","volt","egy","én","te","ő","mi","ti","ők","de","mert",
        "mint","is","vagy","vagyok","le","fel","be","ki","itt","ott"
    }),
    # Slovak
    "sk": frozenset({
        "a","i","v","vo","na","že","sa","si","je","ja","ty","on","ona","ono","my","vy","oni","ale",
        "nie","čo","ako","k","do","za","po","u","od","pre","bez","už"
    }),
    # Slovenian
    "sl": frozenset({
        "in","da","je","se","na","v","za","z","s","ki","kaj","kdo","kot","ali","ne","ja","že","tudi",
        "pri","po","iz","ob"
    }),
    # Chinese (Simplified+Traditional – tokenization-dependent)
    "zh": frozenset({
        "的","了","在","是","不","有","我","他","你","们","这","那","为","上","个","到","说",
        "和","地","就","出","也","可","要","以","会","而","及","与","著","着","之"
    }),
    # Japanese (tokenization-dependent)
    "ja": frozenset({
        "の","に","は","を","た","が","で","て","と","し","ます","です","する","いる","ある",
        "なる","この","その","あの","もの","こと","よう","ため","から","まで","そして","また"
    }),
    # Korean
    "ko": frozenset({
        "이","그","저","것","수","등","들","및","그리고","또는","하지만","그러나","때문에","위해",
        "통해","의","가","을","를","에","에서","로","으로","와","과","도","만","까지","부터","에게",
        "께","보다","처럼","또","또한","혹은","그래서"," 그러나","하면","혹시","이미","아주","매우","너무",
        "좀","또다시","다시","만큼","마다"
    }),
}

# Aliases -> canonical codes (lowercased)
_LANG_ALIASES: dict[str, str] = {
    # English
    "en-us": "en", "en-gb": "en", "eng": "en", "english": "en",
    # Portuguese
    "pt-br": "pt", "pt-pt": "pt", "português": "pt",
    # Chinese
    "zh-cn": "zh", "zh-hans": "zh", "zh-tw": "zh", "zh-hant": "zh", "chinese": "zh",
    # Norwegian
    "nb": "no", "nn": "no",
    # Indonesian/Malay
    "ms-my": "ms", "id-id": "id",
    # Korean/Japanese
    "kor": "ko", "ko-kr": "ko", "jpn": "ja", "ja-jp": "ja",
    # Others
    "de-de": "de", "fr-fr": "fr", "es-es": "es", "it-it": "it", "nl-nl": "nl",
    "ru-ru": "ru", "pl-pl": "pl", "cs-cz": "cs", "tr-tr": "tr", "el-gr": "el",
    "ar-ar": "ar", "fa-ir": "fa", "he-il": "he", "hi-in": "hi", "ur-pk": "ur",
    "bn-bd": "bn", "vi-vn": "vi", "th-th": "th", "ro-ro": "ro", "hu-hu": "hu",
    "sk-sk": "sk", "sl-si": "sl", "fi-fi": "fi", "sv-se": "sv", "da-dk": "da", "no-no": "no",
}

def _canonical_lang(lang: str) -> str:
    """Normalize incoming language codes to our canonical keys."""
    if not lang:
        return "en"
    code = unicodedata.normalize("NFKC", lang.strip().lower())
    code = code.replace("_", "-")
    # direct match, prefix match (e.g., "en-GB" -> "en"), or alias map
    if code in _STOPWORDS:
        return code
    if code in _LANG_ALIASES:
        return _LANG_ALIASES[code]
    # take primary subtag
    primary = code.split("-", 1)[0]
    return _LANG_ALIASES.get(primary, primary if primary in _STOPWORDS else "en")

@lru_cache(maxsize=256)
def _base_stopwords_for(lang: str) -> frozenset[str]:
    """Return the base frozenset for a canonical language code."""
    canon = _canonical_lang(lang)
    base = _STOPWORDS.get(canon)
    if base:
        return base
    # Optional: try NLTK if available and we lack a set
    try:
        from nltk.corpus import stopwords as nltk_stopwords  # type: ignore
        if canon in nltk_stopwords.fileids():
            return frozenset(nltk_stopwords.words(canon))
    except Exception:
        pass
    # Fallback to English
    return _STOPWORDS["en"]

def get_language_stopwords(
    lang: str,
    *,
    extra_stopwords: Iterable[str] | None = None,
    exclude_stopwords: Iterable[str] | None = None,
    aggressive: bool = False,
    include_digits: bool = True,
    fallback_to_english: bool = True,
) -> Set[str]:
    """
    Return a stopword set tailored to the given language, with useful controls.

    Args:
        lang: Language code or name (e.g., 'en', 'en-GB', 'english', 'ko', 'zh-CN').
        extra_stopwords: Additional custom words to include.
        exclude_stopwords: Words to explicitly remove from the set.
        aggressive: If True, adds very common adverbs/particles/functional words where applicable.
        include_digits: If True, treats bare digits ('0'..'9') as stop tokens.
        fallback_to_english: If True, fall back to English when a code is unknown; else return empty set.

    Returns:
        A lowercase set of stopwords appropriate for the language and options provided.

    Notes:
        • For CJK languages (zh/ja/ko), effectiveness depends on your tokenization;
          consider applying a tokenizer before filtering.
        • Ensure your text normalization matches this function (lowercasing, NFKC).
    """
    base = set(_base_stopwords_for(lang))
    if not base and not fallback_to_english:
        return set()

    # Optional aggressive additions per language (lightweight, safe defaults)
    if aggressive:
        canon = _canonical_lang(lang)
        if canon == "en":
            base.update({"also", "still", "ever", "never", "often", "usually", "really"})
        elif canon in {"de","nl"}:
            base.update({"eben","halt","wohl","sehr","immer","oft","wirklich"})
        elif canon == "fr":
            base.update({"toute","tous","toutes","souvent","toujours","vraiment"})
        elif canon == "es":
            base.update({"siempre","nunca","realmente","todavía"})
        elif canon == "it":
            base.update({"sempre","mai","davvero","ancora"})
        elif canon == "pt":
            base.update({"sempre","nunca","realmente","ainda"})
        elif canon == "ru":
            base.update({"всегда","никогда","вообще","реально"})
        elif canon == "tr":
            base.update({"genellikle","aslında","gerçekten"})
        elif canon == "ko":
            base.update({"정말","진짜","항상","보통","자주"})
        elif canon == "ja":
            base.update({"いつも","たいてい","ほんとうに","まったく"})
        elif canon == "zh":
            base.update({"总是","从不","真的","非常","常常"})

    if include_digits:
        base.update(list("0123456789"))

    if extra_stopwords:
        base.update(_normalize_word(w) for w in extra_stopwords if w)

    if exclude_stopwords:
        for w in exclude_stopwords:
            base.discard(_normalize_word(w))

    return base

def _normalize_word(w: str) -> str:
    """Lowercase + NFKC normalize to match stored inventories."""
    return unicodedata.normalize("NFKC", w).lower()