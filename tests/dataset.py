from pydantic import HttpUrl

from models import ArticleEntry

ARTICLE_URL = "https://www.mako.co.il/news-n12_magazine/6a6d777d11485910/Article-9896b0931941691026.htm"
ARTICLES = [
    ArticleEntry(
        title="המהפך המפתיע במדינה שבה כלאו אנשים בכלובים ברחוב",
        subtitle="עריפת ראשו של העיתונאי הבהירה שמי ששולט זה אוסף של כנופיות. פרשנות",
        author="איתי אנגל",
        url=HttpUrl(
            "https://www.mako.co.il/news-n12_magazine/6a6d777d11485910/Article-9896b0931941691026.htm"
        ),
    ),
    ArticleEntry(
        title="התמונה האחרונה של ג'נאן לפני התאונה הקטלנית באיטליה",
        subtitle="החילוץ הסתבך בעקבות מזג האוויר הקשה באזור, המשטרה המקומית חוקרת",
        author="N12",
        url=HttpUrl(
            "https://www.mako.co.il/news-military/f239747af17c5910/Article-3f0026672f74691026.htm"
        ),
    ),
    ArticleEntry(
        title='סער חושף: נפגשתי עם נתניהו בדירת מסתור בת"א',
        subtitle='סיפר בריאיון: "גם אחרי שעזבתי, במרץ 24\', המשכנו להיפגש בחשאי"',
        author="N12",
        url=HttpUrl(
            "https://www.mako.co.il/news-politics/2025_q2/Article-a14f90c3d084691026.htm"
        ),
    ),
    ArticleEntry(
        title="קרוב ל-13 אלף יהודים גרים כאן. למה הם נשארים?",
        subtitle='השכנים מוסתים, היהודים מאוימים: "בתי הכנסת מאובטחים"',
        author="שקד שדה",
        url=HttpUrl(
            "https://www.mako.co.il/news-world/2025_q2/Article-0de0ac4f9f34691026.htm"
        ),
    ),
    ArticleEntry(
        title='הקצין שחשף את האמת שארה"ב הסתירה במשך 80 שנה',
        subtitle="העדויות שהושתקו והדוחות הרשמיים. האם ישראל היא הבאה בתור?",
        author="אלון פדות",
        url=HttpUrl(
            "https://www.mako.co.il/news-world/2025_q2/Article-9eedac1c1244691026.htm"
        ),
    ),
    ArticleEntry(
        title="תכנן לדקור מאבטח בסכין מורעלת ולחטוף לו את הנשק",
        subtitle=None,
        author="אור רביד",
        url=HttpUrl(
            "https://www.mako.co.il/news-law/2025_q2/Article-9d3618ec6284691026.htm"
        ),
    ),
    ArticleEntry(
        title="חמאס לקח הימור מטורף והוכיח שוב: הוא לא מבין את ישראל",
        subtitle=None,
        author='ד"ר הראל חורב',
        url=HttpUrl(
            "https://www.mako.co.il/news-n12_magazine/6a6d777d11485910/Article-a5fb5fe24a41691026.htm"
        ),
    ),
    ArticleEntry(
        title='"אנחנו אנשי ימין, רצינו לטלטל את הממשלה"',
        subtitle=None,
        author="דסק קשת 12",
        url=HttpUrl(
            "https://www.mako.co.il/news-military/f239747af17c5910/Article-5b4a26672f74691026.htm"
        ),
    ),
    ArticleEntry(
        title="עמית נלחמה בעשרות מחבלים, עד שנפצעה",
        subtitle=None,
        author="יעל אודם",
        url=HttpUrl(
            "https://www.mako.co.il/news-israel/2025_q2/Article-af8a42808d74691026.htm"
        ),
    ),
    ArticleEntry(
        title='"ידידת אמת בכל זמן": המדינה שמחכה לישראלים',
        subtitle=None,
        author="אילן ארנון",
        url=HttpUrl(
            "https://www.mako.co.il/news-world/2025_q2/Article-981f1afb1ba3691026.htm"
        ),
    ),
]
