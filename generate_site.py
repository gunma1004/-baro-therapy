import os
import random
from urllib.parse import quote

seoul_data = {
    'jongno': {'name': '종로구', 'dongs': ['청운동', '효자동', '사직동', '삼청동', '부암동', '평창동', '무악동', '교남동', '가회동', '종로1.2.3.4가동', '종로5.6가동', '이화동', '혜화동', '창신1동', '창신2동', '창신3동', '숭인1동', '숭인2동']},
    'jung': {'name': '중구', 'dongs': ['소공동', '회현동', '명동', '필동', '장충동', '광희동', '을지로동', '신당동', '다산동', '약수동', '청구동', '동화동', '황학동', '중림동']},
    'yongsan': {'name': '용산구', 'dongs': ['후암동', '용산2가동', '남영동', '청파동', '원효로1동', '원효로2동', '효창동', '용문동', '이촌1동', '이촌2동', '이태원1동', '이태원2동', '한남동', '서빙고동', '보광동']},
    'seongdong': {'name': '성동구', 'dongs': ['왕십리2동', '왕십리도선동', '마장동', '사근동', '행당1동', '행당2동', '응봉동', '금호1가동', '금호2.3가동', '금호4가동', '옥수동', '성수1가1동', '성수1가2동', '성수2가1동', '성수2가3동', '송정동', '용답동']},
    'gwangjin': {'name': '광진구', 'dongs': ['중곡1동', '중곡2동', '중곡3동', '중곡4동', '능동', '구의1동', '구의2동', '구의3동', '광장동', '자양1동', '자양2동', '자양3동', '자양4동', '화양동', '군자동']},
    'dongdaemun': {'name': '동대문구', 'dongs': ['신설동', '용두동', '제기동', '전농1동', '전농2동', '답십리1동', '답십리2동', '장안1동', '장안2동', '청량리동', '회기동', '휘경1동', '휘경2동', '이문1동', '이문2동']},
    'jungnang': {'name': '중랑구', 'dongs': ['면목본동', '면목2동', '면목3.4동', '면목5동', '면목7동', '상봉1동', '상봉2동', '중화1동', '중화2동', '묵1동', '묵2동', '망우본동', '망우3동', '신내1동', '신내2동']},
    'seongbuk': {'name': '성북구', 'dongs': ['성북동', '삼선동', '동선동', '돈암1동', '돈암2동', '안암동', '보문동', '정릉1동', '정릉2동', '정릉3동', '정릉4동', '길음1동', '길음2동', '종암동', '월곡1동', '월곡2동', '장위1동', '장위2동', '장위3동', '석관동']},
    'gangbuk': {'name': '강북구', 'dongs': ['삼양동', '미아동', '송중동', '송천동', '삼각산동', '번1동', '번2동', '번3동', '수유1동', '수유2동', '수유3동', '우이동', '인수동']},
    'dobong': {'name': '도봉구', 'dongs': ['창1동', '창2동', '창3동', '창4동', '창5동', '도봉1동', '도봉2동', '쌍문1동', '쌍문2동', '쌍문3동', '쌍문4동', '방학1동', '방학2동', '방학3동']},
    'nowon': {'name': '노원구', 'dongs': ['상계1동', '상계2동', '상계3.4동', '상계5동', '상계6.7동', '상계8동', '상계9동', '상계10동', '중계본동', '중계1동', '중계2.3동', '중계4동', '하계1동', '하계2동', '공릉1동', '공릉2동']},
    'eunpyeong': {'name': '은평구', 'dongs': ['불광1동', '불광2동', '갈현1동', '갈현2동', '구산동', '대조동', '응암1동', '응암2동', '응암3동', '역촌동', '신사1동', '신사2동', '증산동', '수색동', '진관동']},
    'seodaemun': {'name': '서대문구', 'dongs': ['천연동', '북아현동', '충현동', '신촌동', '연희동', '홍제1동', '홍제2동', '홍제3동', '홍은1동', '홍은2동', '남가좌1동', '남가좌2동', '북가좌1동', '북가좌2동']},
    'mapo': {'name': '마포구', 'dongs': ['공덕동', '아현동', '도화동', '용강동', '대흥동', '염리동', '신수동', '서교동', '합정동', '망원1동', '망원2동', '연남동', '성산1동', '성산2동', '상암동']},
    'yangcheon': {'name': '양천구', 'dongs': ['목1동', '목2동', '목3동', '목4동', '목5동', '신월1동', '신월2동', '신월3동', '신월4동', '신월5동', '신월6동', '신월7동', '신정1동', '신정2동', '신정3동', '신정4동', '신정6동', '신정7동']},
    'gangseo': {'name': '강서구', 'dongs': ['등촌1동', '등촌2동', '등촌3동', '화곡본동', '화곡1동', '화곡2동', '화곡3동', '화곡4동', '화곡8동', '우장산동', '가양1동', '가양2동', '가양3동', '발산1동', '공항동', '방화1동', '방화2동', '방화3동']},
    'guro': {'name': '구로구', 'dongs': ['신도림동', '구로1동', '구로2동', '구로3동', '구로4동', '구로5동', '가리봉동', '고척1동', '고척2동', '개봉1동', '개봉2동', '개봉3동', '오류1동', '오류2동', '수궁동']},
    'geumcheon': {'name': '금천구', 'dongs': ['가산동', '독산1동', '독산2동', '독산3동', '독산4동', '시흥1동', '시흥2동', '시흥3동', '시흥4동', '시흥5동']},
    'yeongdeungpo': {'name': '영등포구', 'dongs': ['영등포본동', '영등포동', '여의동', '당산1동', '당산2동', '도림동', '문래동', '양평1동', '양평2동', '신길1동', '신길3동', '신길4동', '신길5동', '신길6동', '신길7동', '대림1동', '대림2동', '대림3동']},
    'dongjak': {'name': '동작구', 'dongs': ['노량진1동', '노량진2동', '상도1동', '상도2동', '상도3동', '상도4동', '흑석동', '사당1동', '사당2동', '사당3동', '사당4동', '사당5동', '대방동', '신대방1동', '신대방2동']},
    'gwanak': {'name': '관악구', 'dongs': ['보라매동', '청림동', '성현동', '행운동', '낙성대동', '청룡동', '은천동', '상현동', '서원동', '신원동', '서림동', '신사동', '난향동', '조원동', '대학동', '난곡동', '삼성동', '미성동']},
    'seocho': {'name': '서초구', 'dongs': ['서초1동', '서초2동', '서초3동', '서초4동', '잠원동', '반포본동', '반포1동', '반포2동', '반포3동', '반포4동', '방배본동', '방배1동', '방배2동', '방배3동', '방배4동', '양재1동', '양재2동', '내곡동']},
    'gangnam': {'name': '강남구', 'dongs': ['역삼1동', '역삼2동', '개포1동', '개포2동', '개포4동', '청담동', '삼성1동', '삼성2동', '대치1동', '대치2동', '대치4동', '신사동', '논현1동', '논현2동', '압구정동', '세곡동', '자곡동', '일원동', '수서동', '도곡1동', '도곡2동']},
    'songpa': {'name': '송파구', 'dongs': ['잠실본동', '잠실2동', '잠실3동', '잠실4동', '잠실6동', '잠실7동', '풍납1동', '풍납2동', '거여1동', '거여2동', '마천1동', '마천2동', '방이1동', '방이2동', '오륜동', '오금동', '송파1동', '송파2동', '석촌동', '삼전동', '가락본동', '가락1동', '가락2동', '문정1동', '문정2동', '장지동', '위례동', '잠실동']},
    'gangdong': {'name': '강동구', 'dongs': ['강일동', '상일1동', '상일2동', '명일1동', '명일2동', '고덕1동', '고덕2동', '암사1동', '암사2동', '암사3동', '천호1동', '천호2동', '천호3동', '성내1동', '성내2동', '성내3동', '둔촌1동', '둔촌2동']}
}

# [핵심 4번 반영] 고가치 주력 동네 타겟팅 (수동 최적화를 위해 일단 돈 되는 곳만 뽑아냅니다)
# 전체 25개 구를 다 뽑으려면 아래 리스트를 비우거나 주석 처리하세요: TARGET_GUS = []
TARGET_GUS = ['강남구', '서초구', '종로구', '마포구'] 

site_name = "바로테라피"
base_url = "https://baro-therapy.netlify.app"
base_dir = "output"
os.makedirs(base_dir, exist_ok=True)

# [핵심 1번 반영] 권역별 큐레이션을 위한 업체 리스트 분리
comp_group_A = [
    {"name": "퀸즈홈테라피", "tel": "0507-1280-3296"},
    {"name": "한국미인테라피", "tel": "0507-1280-3140"},
    {"name": "오늘밤테라피", "tel": "0507-1280-3199"}
]
comp_group_B = [
    {"name": "주주테라피", "tel": "0507-1280-3197"},
    {"name": "기쁨테라피", "tel": "0507-1280-3183"},
    {"name": "미인클럽테라피", "tel": "0507-1280-3180"}
]
gangnam_circle = ['강남구', '서초구', '송파구', '강동구', '동작구', '관악구'] # A그룹 우선 배정 권역

# 텍스트 스피닝용 데이터 풀
leads_sub = [
    "씻을 기운조차 없는 날이 있죠. 제휴 업체가 편안함을 안고 {dong} 출장마사지로 찾아갑니다.",
    "끝나고 캐모마일 차 한 잔이면 밤이 짧아지는 날. {dong} 출장마사지 고객님을 위한 케어입니다.",
    "조용히 위로받고 싶은 날, 전문 테라피스트가 {dong} 출장마사지 예약에 맞춰 방문합니다."
]
intro_phrases = ["집게핀으로 대충 올린 날.", "발바닥이 뜨거운 날.", "어제 요가를 했는데 어깨가 더 뭉친 날.", "머리가 복잡한 날."]
chat_pool = [
    ("아로마 오일 테라피는 향이 세지 않나요?", "향이 먼저 들어오고 손이 뒤따르는 정도입니다."),
    ("머리를 수건으로 감싼 채인데 괜찮나요?", "네. 그 상태 그대로 문만 열어 주시면 됩니다."),
    ("받기 전에 꼭 씻어야 하나요?", "꼭 하지 않으셔도 됩니다. 편한 대로 하세요.")
]
review_pool = [
    ("H님", "스페셜 테라피 120분", "손목을 조심히 다뤄 주는 점이 좋았어요. 제가 불편해하는 곳이라 더 기억에 남죠."),
    ("곽OO", "아로마 오일 테라피 60분", "쓰던 베개로 받으니 마음이 편했어요. 높이가 익숙해서 더 그랬겠죠.")
]
faq_pool = [
    ("오일 냄새 오래 가나요", "세 코스 모두 오일을 씁니다. 걱정되면 문자에 적어 주세요."),
    ("숙소도 되나요", "네, 호텔이나 숙소로도 방문 가능합니다.")
]
rules_pool = [
    "약속한 시간에 맞춰 갑니다. 늦으면 먼저 문자로 알립니다.",
    "문자를 보내면 상담 담당자가 10분 안에 답합니다."
]

# 공통 CSS 
COMMON_CSS = """
:root{--mint:#48c8c0;--mint-d:#2aa9a1;--mint-l:#f3fbfa;--ink:#202020;--sub:#7d8387;--soft:#a0a4a4;--line:#e6e8ea;--gray:#f9f9f9;--fill:#f1f2f3}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;overflow-x:hidden}
body{background:#fff;color:var(--ink);font-family:"Pretendard Variable",system-ui,sans-serif;font-size:15.5px;line-height:1.75;word-break:keep-all;-webkit-font-smoothing:antialiased;}
a{color:inherit;text-decoration:none}
.wrap{width:min(90vw,640px);margin-inline:auto}
.serif{font-family:"Noto Serif KR",serif}
header.bar{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.bar .wrap{display:flex;align-items:center;justify-content:space-between;height:58px}
.logo{font-weight:800;font-size:17px;display:flex;align-items:center;gap:8px}
.logo b{width:9px;height:9px;border-radius:50%;background:var(--mint)}
.pill{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 20px;border-radius:999px;font-weight:700;font-size:14.5px;background:var(--mint);color:#fff;transition:transform .15s}
.pill.lg{min-height:54px;padding:0 30px;font-size:16.5px}
.hero{text-align:center;padding:56px 0 30px}
.hero h1{font-size:clamp(27px,7.4vw,40px);line-height:1.3;font-weight:500;letter-spacing:-.03em}
.hero .lead{margin:16px auto 0;color:var(--sub);font-size:15px}
.hero .cta{display:flex;gap:10px;justify-content:center;margin-top:26px}
.sec{padding:50px 0 72px;text-align:center}
.sec.gray{background:var(--gray)}
h2{font-size:clamp(22px,6vw,30px);line-height:1.35;font-weight:500;letter-spacing:-.03em}
h2 em{font-style:normal;color:var(--mint-d)}
.sub{color:var(--sub);font-size:14.5px;margin-top:10px}
.companies-grid { display:grid; gap:12px; margin:26px auto 0; max-width:560px; text-align:left; grid-template-columns:1fr 1fr; }
.companies-grid a { background:#fff; border:1px solid var(--line); border-radius:14px; padding:20px 18px; display:block; transition:border-color .15s; }
.companies-grid h3 { font-size:16px; color:var(--ink); margin-bottom:4px; font-weight:800; }
.companies-grid p { font-size:15px; color:var(--mint-d); font-weight:700; }
.chat{list-style:none;margin:26px auto 0;max-width:520px;display:grid;gap:10px;text-align:left}
.chat li{max-width:86%;padding:12px 16px;border-radius:18px;font-size:14.5px;line-height:1.6;color:#3a3f43;background:var(--fill);border-bottom-left-radius:6px;justify-self:start}
.chat li.me{background:var(--mint-l);border:1px solid #cdeeeb;border-bottom-left-radius:18px;border-bottom-right-radius:6px;justify-self:end;color:var(--ink)}
.check{list-style:none;margin:26px auto 0;max-width:560px;text-align:left;display:grid;gap:10px}
.check li{position:relative;padding:14px 16px 14px 44px;background:#fff;border:1px solid var(--line);border-radius:12px;font-size:15px;font-weight:600}
.check li::before{content:"";position:absolute;left:16px;top:19px;width:7px;height:12px;border:solid var(--mint);border-width:0 2.5px 2.5px 0;transform:rotate(45deg)}
.strip{display:grid;gap:12px;margin:26px auto 0;max-width:560px;text-align:left;grid-template-columns:1fr 1fr}
.strip figure{background:#fff;border-radius:16px;padding:20px 18px;border:1px solid var(--line);display:grid;gap:14px;align-content:space-between}
.strip blockquote{font-size:15px;line-height:1.7;color:#3a3f43}
.faq{display:grid;gap:12px;margin:26px auto 0;max-width:560px;text-align:left;grid-template-columns:1fr 1fr}
.faq div{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px 18px}
.faq .q{font-weight:800;font-size:15.5px;margin-bottom:8px}
.faq .a{color:var(--sub);font-size:14.5px}
.chips{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:26px auto 0;max-width:560px}
.chips a{display:inline-flex;align-items:center;justify-content:center;min-height:44px;background:#fff;border:1px solid var(--line);border-radius:999px;font-size:13.5px;font-weight:600;padding:4px 16px;transition:background .15s}
footer{background:#2b2f33;color:#fff;padding:40px 0 48px;text-align:center}
.fab{position:fixed;right:16px;bottom:18px;z-index:30;width:66px;height:66px;border-radius:50%;background:var(--mint);color:#fff;display:grid;place-items:center;text-align:center;font-size:12px;font-weight:800;line-height:1.2}
@media(max-width:480px) { .companies-grid, .strip, .faq { grid-template-columns:1fr; } }
"""

# [핵심 2번 유지] 계층형 피라미드 링크
def get_hierarchical_chips(level, gu_key=None, target_data=seoul_data):
    chips = []
    if level == 'main':
        for g_key, g_info in target_data.items():
            chips.append(f'<a href="{base_url}/{quote(g_info["name"])}/">{g_info["name"]}</a>')
    elif level == 'gu' and gu_key:
        dongs = target_data[gu_key]['dongs']
        for dong in dongs:
            chips.append(f'<a href="{base_url}/{quote(dong)}/">{dong}</a>')
    elif level == 'dong' and gu_key:
        dongs = target_data[gu_key]['dongs']
        sample_size = min(5, len(dongs)) # 주변 지역 5개만 추출
        sampled_dongs = random.sample(dongs, sample_size)
        for dong in sampled_dongs:
            chips.append(f'<a href="{base_url}/{quote(dong)}/">{dong}</a>')
    return "\n".join(chips)

# HTML 템플릿 엔진
def generate_html(location_name, url_path, level, gu_key=None, gu_name_kor=None, target_data=seoul_data):
    
    # 텍스트 셔플링
    intro = random.choice(intro_phrases)
    chats = random.sample(chat_pool, min(2, len(chat_pool)))
    chat_html = "".join([f'<li><small>손님</small>{q}</li><li class="me"><small>{site_name}</small>{a}</li>' for q, a in chats])
    reviews = random.sample(review_pool, min(2, len(review_pool)))
    reviews_html = "".join([f'<figure><blockquote>{txt}</blockquote><figcaption><span><b>{name}</b><br>{course}</span></figcaption></figure>' for name, course, txt in reviews])
    faqs = random.sample(faq_pool, min(2, len(faq_pool)))
    faq_html = "".join([f'<div><p class="q">{q}</p><p class="a">{a}</p></div>' for q, a in faqs])
    rules = random.sample(rules_pool, min(2, len(rules_pool)))
    rules_html = "".join([f'<li>{r}</li>' for r in rules])
    
    # [핵심 1번 로직] 권역에 따른 업체 리스트 큐레이션 및 셔플
    top_comps = []
    bottom_comps = []
    if gu_name_kor in gangnam_circle:
        top_comps = comp_group_A.copy()
        bottom_comps = comp_group_B.copy()
    else:
        top_comps = comp_group_B.copy()
        bottom_comps = comp_group_A.copy()
        
    random.shuffle(top_comps)
    random.shuffle(bottom_comps)
    final_companies = top_comps + bottom_comps # 강남권이면 퀸즈,한국미인,오늘밤이 상단 3개 무작위 장악
    
    companies_html = ""
    json_ld_items = []
    for idx, comp in enumerate(final_companies, 1):
        companies_html += f'<a href="tel:{comp["tel"]}"><h3>{comp["name"]}</h3><p>{comp["tel"]}</p></a>\n'
        json_ld_items.append(f'{{"@type": "LocalBusiness", "position": {idx}, "name": "{comp["name"]}", "telephone": "{comp["tel"]}"}}')
    json_ld_str = ",\n        ".join(json_ld_items)

    # 텍스트 설정
    if level == 'main':
        title = f"{site_name} | 프리미엄 스웨디시 홈테라피"
        desc = f"{site_name}에서 검증된 프리미엄 홈테라피 업체를 만나보세요."
        h1_text = "프리미엄 테라피<br>스웨디시 홈테라피"
        lead_text = f"씻을 기운조차 없는 날이 있죠. {site_name} 제휴 업체가 찾아갑니다."
        section_title = f"{site_name} 제휴 업체"
        chips_title = "서울 지역 안내"
    else:
        title = f"{location_name} 출장마사지 프리미엄 테라피 | {site_name}"
        desc = f"{location_name} 출장마사지 {site_name}에서 검증된 홈테라피 업체를 만나보세요."
        h1_text = f"{location_name} 출장마사지<br>프리미엄 홈테라피"
        lead_text = random.choice(leads_sub).format(dong=location_name)
        section_title = f"{location_name} 출장마사지 제휴 업체"
        chips_title = "주변 동네" if level == 'dong' else f"{location_name} 지역 안내"

    chips_html = get_hierarchical_chips(level, gu_key, target_data)

    # [핵심 3번 로직] 업체 리스트를 포함한 100% DOM 무작위 배치
    # 이 배열 안의 HTML 덩어리들이 매 페이지마다 위아래 순서가 완전히 뒤바뀝니다.
    section_blocks = [
        f'<section id="companies" class="sec gray"><div class="wrap"><h2 class="serif"><em>{section_title}</em></h2><div class="companies-grid">{companies_html}</div></div></section>',
        f'<section class="sec"><div class="wrap"><h2 class="serif"><em>이런 날</em> 이런 몸</h2><ul class="chat">{chat_html}</ul></div></section>',
        f'<section class="sec gray"><div class="wrap"><h2 class="serif"><em>받아 본 분들의</em> 리뷰</h2><div class="strip">{reviews_html}</div></div></section>',
        f'<section class="sec"><div class="wrap"><h2 class="serif"><em>지키는 것,</em> 하지 않는 것</h2><ul class="check">{rules_html}</ul></div></section>',
        f'<section class="sec gray"><div class="wrap"><h2 class="serif"><em>궁금한</em> 것부터</h2><div class="faq">{faq_html}</div></div></section>'
    ]
    random.shuffle(section_blocks)
    dynamic_dom_content = "\n".join(section_blocks)

    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url_path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<script>
  document.addEventListener("DOMContentLoaded", function() {{
    const jsonLd = {{
      "@context": "https://schema.org",
      "@type": "ItemList",
      "url": "{url_path}",
      "name": document.title,
      "itemListElement": [
        {json_ld_str}
      ]
    }};
    const script = document.createElement('script');
    script.type = "application/ld+json";
    script.text = JSON.stringify(jsonLd);
    document.head.appendChild(script);
  }});
</script>
<style>{COMMON_CSS}</style>
</head>
<body class="root">
<header class="bar"><div class="wrap"><a class="logo" href="{base_url}/"><b></b>{site_name}</a><a class="pill" href="#companies">제휴 업체</a></div></header>

<section class="hero">
<div class="wrap">
<h1 class="serif">{h1_text}</h1>
<p class="lead">{lead_text}</p>
<div class="cta"><a class="pill lg" href="#companies">업체 바로보기</a></div>
</div>
</section>

<!-- 무작위로 섞인 5개 섹션 (업체 리스트 포함) 출력 구역 -->
{dynamic_dom_content}

<section class="sec"><div class="wrap"><h2 class="serif"><em>{chips_title}</em></h2>
<div class="chips">
{chips_html}
</div></div></section>

<footer>
<div class="wrap"><div class="logo" style="justify-content:center;color:#fff;font-size:19px;"><b></b>{site_name}</div><p style="color:#b8bcc0;font-size:14px;margin-top:10px;">프리미엄 테라피 안내</p></div>
</footer>
<a class="fab" href="#companies">업체<br>보기</a>
</body>
</html>
"""

# 필터링 로직 (핵심 타겟 구만 뽑아냅니다)
filtered_seoul_data = {}
if TARGET_GUS:
    for k, v in seoul_data.items():
        if v['name'] in TARGET_GUS:
            filtered_seoul_data[k] = v
else:
    filtered_seoul_data = seoul_data

sitemap_urls = [f"{base_url}/"]

# 메인 페이지 생성
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(generate_html("서울 전지역", f"{base_url}/", level='main', target_data=filtered_seoul_data))

# 구/동 페이지 생성
for gu_key, gu_info in filtered_seoul_data.items():
    gu_name = gu_info['name']
    
    gu_folder = os.path.join(base_dir, gu_name)
    os.makedirs(gu_folder, exist_ok=True)
    gu_url = f"{base_url}/{quote(gu_name)}/"
    sitemap_urls.append(gu_url)
    
    with open(os.path.join(gu_folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_html(gu_name, gu_url, level='gu', gu_key=gu_key, gu_name_kor=gu_name, target_data=filtered_seoul_data))
    
    for dong in gu_info['dongs']:
        dong_folder = os.path.join(base_dir, dong)
        os.makedirs(dong_folder, exist_ok=True)
        dong_url = f"{base_url}/{quote(dong)}/"
        sitemap_urls.append(dong_url)
        
        with open(os.path.join(dong_folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(generate_html(dong, dong_url, level='dong', gu_key=gu_key, gu_name_kor=gu_name, target_data=filtered_seoul_data))

# Sitemap & Robots 생성
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_content += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n  </url>\n"
sitemap_content += '</urlset>'

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)

with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {base_url}/sitemap.xml\n")

print(f"✅ 바로테라피 스팸방지 100% 적용 스크립트 완료! (타겟 지역: {TARGET_GUS if TARGET_GUS else '전체'})")