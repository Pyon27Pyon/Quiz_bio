import streamlit as st
import random

st.title("生化学 ランダム単語帳テスト")

# セッション状態の初期化
if 'questions' not in st.session_state:
    # 54問の問題データ
    st.session_state.all_questions = [
        # --- セクション1 ---
        {"text": "アミノ酸からケトグルタル酸へαアミノ基を転移する酵素を【  】と呼ぶ。", "answer": "アミノ基転移酵素"},
        {"text": "窒素が筋肉から肝臓へ輸送される際は、窒素が【  】やグルタミンに組み込まれた形で行われる。", "answer": "アラニン"},
        {"text": "【  】は NAD+や NADP+を利用して酸化的脱アミノ反応を司る酵素である。", "answer": "グルタミン酸脱水素酵素"},
        {"text": "アミノ基転位反応によってアスパラギン酸とケトグルタル酸から【  】とグルタミン酸が生じる。", "answer": "オキサロ酢酸"},
        {"text": "メチオニンの分解過程で生じる【  】はメチル基の供与体として機能する。", "answer": "S-アデノシルメチオニン(SAM)"},
        {"text": "アミノ酸の異化反応に不可欠なビタミンは【  】である。", "answer": "ビタミン B6"},
        {"text": "生物における芳香環の開裂反応の殆どは【  】という酵素によって行われる。", "answer": "ジオキシゲナーゼ"},
        {"text": "分枝鎖ケト酸脱水素酵素複合体の遺伝的欠失によって生じる疾患は【  】である。", "answer": "メープルシロップ尿症"},
        {"text": "異化反応の結果、その炭素骨格が糖新生を介してグルコースに置換され得るアミノ酸を【  】と呼ぶ。", "answer": "糖原性アミノ酸"},
        {"text": "アミノ酸の窒素原子は、大元は【  】に由来する。", "answer": "大気中の窒素"},
        {"text": "セリン・システイン・グリシンの炭素骨格は【  】に由来する。", "answer": "3-ホスホグリセリン酸"},
        {"text": "【  】は活性化一炭素供与体として様々な生体反応に関与する。", "answer": "テトラヒドロ葉酸(THF)"},
        {"text": "メチオニンの分解過程で生じる【  】は、血中に過剰に存在すると動脈硬化などを引き起こす恐れがあるとされている。", "answer": "ホモシステイン"},
        {"text": "一酸化窒素はアミノ酸の一種【  】の酸化によって生じる。", "answer": "アルギニン"},
        {"text": "殆どのアミノ酸のαアミノ基は【  】からアミノ基転位反応で供給される。", "answer": "グルタミン酸"},
        {"text": "グルタミン酸はグルタミン・アルギニン・【  】の前駆体である。", "answer": "プロリン"},
        {"text": "メチオニン合成酵素の補酵素であるメチルコバラミンは【  】の誘導体であり、その機能は葉酸の生産にも重要である。", "answer": "ビタミン B12"},
        {"text": "ヒスチジン、ロイシン、フェニルアラニンなどの【  】アミノ酸の生合成には多くの反応が必要である。", "answer": "必須"},
        
        # --- セクション2 ---
        {"text": "大腸菌での翻訳過程で tRNA をリボソームの A 部位に運ぶ因子は【  】である。", "answer": "EF-Tu"},
        {"text": "イノシンは tRNA 上の【  】という部位にしばしば存在する。", "answer": "アンチコドン(アンチコドンループ)"},
        {"text": "原核生物で一本の mRNA に複数の遺伝子がコードされる様態を【  】と呼ぶ。", "answer": "ポリシストロニック"},
        {"text": "原核生物のタンパク質の最初(N 末端)のアミノ酸は【  】である。", "answer": "N-ホルミルメチオニン"},
        {"text": "tRNA とそれに適切なアミノ酸とを結合させるのは【  】である。", "answer": "アミノアシル tRNA 合成酵素"},
        {"text": "リボソームが持つ、ペプチド結合を作る酵素活性を【  】活性と呼ぶ。", "answer": "ペプチジルトランスフェラーゼ"},
        {"text": "翻訳開始時にリボソームの P 部位にアミノ酸を輸送するのは【  】である。", "answer": "IF-2"},
        {"text": "哺乳類において【  】は mRNA の 5’キャップに結合し、インスリンによる翻訳開始促進作用を仲介する。", "answer": "eIF-4E"},
        {"text": "【  】は EF2 に異常な修飾を施し、その機能を阻害するので真核生物の翻訳機構を阻害する。", "answer": "ジフテリア毒素"},
        {"text": "開始コドンは特異的な tRNA によって、終止コドンは【  】によってそれぞれ認識される。", "answer": "RF(RF1, RF2)"},
        {"text": "翻訳の開始・伸長・終結の全てのステップにおいて【  】ファミリーに属するタンパク質の働きが必要である。", "answer": "G タンパク質"},
        {"text": "ユビキチン化されたタンパク質の分解は【  】によって行われる。", "answer": "プロテアソーム"},
        {"text": "ユビキチン化されるタンパク質は【  】と呼ばれる酵素のファミリーによって認識される。", "answer": "E3(ユビキチンリガーゼ)"},
        {"text": "【  】と呼ばれるシステムにより、必要な場合には細胞質内の一部が丸ごと分解されることもある。その際、分解する領域を【  】と呼ばれる構造が取り囲む。", "answer": "オートファジー / オートファゴソーム"},
        {"text": "細胞内小器官の一つである【  】の内部の pH は非常に低く、また多様なタンパク質分解酵素を含んでいるため、様々な生体高分子の分解の場となっている。", "answer": "リソソーム"},
        {"text": "複数のコドンが同一のアミノ酸をコードすることを遺伝暗号の【  】と言う。", "answer": "縮重"},
        {"text": "真核生物の mRNA の最も 3’側には【  】が存在し、翻訳の促進や mRNA の安定性に寄与している。", "answer": "poly A tail"},
        {"text": "真核生物の mRNA の 3’UTR には【  】の結合部位が存在するため、翻訳阻害や mRNA の分解を通じ、状況に応じた様々な生体機能の制御が可能になっている。", "answer": "miRNA"},
        
        # --- セクション3 ---
        {"text": "哺乳類では生体内に過剰に存在する NH4+は最終的に【  】に置換される。", "answer": "尿素"},
        {"text": "尿素サイクルの最初のステップでは HCO3- と NH4+から【  】が合成される。", "answer": "カルバモイルリン酸"},
        {"text": "尿素サイクルにおいて、アルギニンが分解されると【  】と【  】が生成される。", "answer": "オルニチン / 尿素"},
        {"text": "【  】塩基は de novo 経路と salvage 経路の両方の経路で合成される。", "answer": "プリン"},
        {"text": "アデニル酸(AMP)の合成にはエネルギー源に【  】を用いるが、これは他のヌクレオチドの合成反応では見られない特徴である。", "answer": "グアノシン三リン酸(GTP)"},
        {"text": "プリンもしくはピリミジン塩基が糖と結合した分子を【  】と呼ぶ。", "answer": "ヌクレオシド"},
        {"text": "プリンもしくはピリミジン塩基が糖とリン酸エステルに結合した分子を【  】と呼ぶ。", "answer": "ヌクレオチド"},
        {"text": "シチジン三リン酸(CTP)は【  】がアミノ化することで合成される。", "answer": "ウリジン三リン酸(UTP)"},
        {"text": "イノシン酸(IMP)からグアニル酸(GMP)を合成する過程で【  】が合成される。", "answer": "キサンチル酸(XMP)"},
        {"text": "プリンヌクレオチド異化反応過程に必要な【  】と呼ばれる酵素の遺伝的欠失は、リンパ球の機能不全から重篤な免疫不全症を引き起こす。", "answer": "アデノシンデアミナーゼ(ADA)"},
        {"text": "プリン塩基の霊長類での最終代謝産物は【  】である。", "answer": "尿酸(塩)"},
        {"text": "血中尿酸値が過度に高いと【  】と呼ばれる疾患に至る場合がある。これは体内に蓄積した尿酸塩が結晶化し、関節などで炎症を引き起こすことで発症する。", "answer": "痛風"},
        {"text": "グリシン、グルタミンおよび【  】の3つのアミノ酸がプリン塩基の環構造の材料となる。", "answer": "アスパラギン酸"},
        {"text": "【  】の de novo 合成では塩基が合成されたのちにリボースと結合する。", "answer": "ピリミジン"},
        {"text": "HPRT (HGPRT)はグアニル酸(GMP)と【  】の合成を触媒する。", "answer": "イノシン酸(IMP)"},
        {"text": "5-フルオロウラシルは体内で代謝され、その産物が【  】と拮抗することでチミジル酸(TMP)の合成を抑制する。", "answer": "デオキシウリジン一リン酸(dUMP)"},
        {"text": "ジヒドロ葉酸還元酵素はチミジル酸(TMP)合成に必須の酵素であり、【  】などの抗癌剤の良いターゲットとなっている。", "answer": "メトトレキサート(アミノプテリン)"},
        {"text": "HPRT (HGPRT)の遺伝的欠失は【  】という疾患の要因となる。", "answer": "レッシュ・ナイハン症候群"}
    ]
    # 現在のテスト用リストに全問題をコピーしてシャッフル
    st.session_state.questions = st.session_state.all_questions.copy()
    random.shuffle(st.session_state.questions)
    
    st.session_state.current_q = 0
    st.session_state.show_answer = False
    st.session_state.review_list = [] # わからなかった問題を保存するリスト

total = len(st.session_state.questions)
current = st.session_state.current_q

if current < total:
    st.write(f"**【第{current + 1}問 / 全{total}問】**")
    q = st.session_state.questions[current]
    
    # 問題文を表示
    st.info(q["text"])

    # まだ答えを見ていない場合
    if not st.session_state.show_answer:
        if st.button("答えを見る"):
            st.session_state.show_answer = True
            st.rerun()
            
    # 答えを見た後の表示
    else:
        st.success(f"**正解： {q['answer']}**")
        
        st.write("この問題、わかりましたか？")
        # 横並びに2つのボタンを配置
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("⭕ わかった（次へ）", use_container_width=True):
                st.session_state.current_q += 1
                st.session_state.show_answer = False
                st.rerun()
                
        with col2:
            if st.button("❌ チェックして次へ", use_container_width=True):
                # わからなかった問題をreview_listに追加
                st.session_state.review_list.append(q)
                st.session_state.current_q += 1
                st.session_state.show_answer = False
                st.rerun()

# 全問終了後の画面
else:
    st.write("---")
    st.subheader("すべての問題が終了しました！お疲れ様でした。")
    
    review_count = len(st.session_state.review_list)
    
    if review_count > 0:
        st.warning(f"今回は **{review_count}問** の問題にチェックがつきました。")
        
        # チェックした問題の一覧をアコーディオン（折りたたみ）で表示
        with st.expander("チェックした問題と解答を確認する"):
            for i, rq in enumerate(st.session_state.review_list):
                st.write(f"**{i+1}.** {rq['text']}  \n👉 **正解:** {rq['answer']}")
                st.write("---")
        
        st.write(" ") # 少し余白を空ける
        
        # 復習モード開始ボタン
        if st.button("💡 チェックした問題だけをやり直す"):
            # review_listの問題だけをセットして再スタート
            st.session_state.questions = st.session_state.review_list.copy()
            random.shuffle(st.session_state.questions)
            st.session_state.current_q = 0
            st.session_state.show_answer = False
            st.session_state.review_list = [] # 復習リストをリセット
            st.rerun()
            
    else:
        st.success("素晴らしい！全問完璧に「わかった」と回答しました！")

    st.write("---")
    # 完全リセットボタン（全54問から再スタート）
    if st.button("🔄 最初から全問シャッフルしてやり直す"):
        st.session_state.clear()
        st.rerun()
