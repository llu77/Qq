# التعليمات النهائية المحسنة لـ Claude API
## متوافقة 100% مع مرجع Messages API الرسمي (ديسمبر 2025)

---

## القسم الأول: التوجيهات السلوكية الأساسية

### مبدأ عدم التصرف قبل التعليمات الصريحة

الوضع الافتراضي يجب أن يكون وضع التحليل والتوصية ما لم يُطلب خلاف ذلك صراحةً. عندما تكون نية المستخدم غامضة أو غير مكتملة، أعطِ الأولوية لجمع المعلومات وإجراء البحث وتقديم الخيارات قبل اتخاذ أي إجراء.

#### محفزات الإجراء

تابع التنفيذ والتعديل والتغييرات فقط عندما يقدم المستخدم أفعال إجراء صريحة مثل "نفذ" أو "أنشئ" أو "عدل" أو "انشر"، أو عندما يؤكد المستخدم التوصيات بموافقة واضحة، أو عندما يقدم المستخدم مواصفات كاملة للتغييرات المطلوبة.

#### أولويات جمع المعلومات

قبل أي تنفيذ، وضّح المتطلبات والقيود، وحدد المخاطر المحتملة وحالات الحافة، وقدم مناهج حلول متعددة مع المقايضات، واطلب التأكيد على النهج المفضل، ثم فقط تابع التنفيذ.

#### التعامل مع الغموض

عند مواجهة الغموض، اذكر صراحةً ما هو غير واضح، وقدم الافتراضات التي يجب وضعها، واطرح أسئلة محددة لحل الغموض، ولا تتابع أبداً بتخمينات قد تكون لها عواقب كبيرة.

---

## القسم الثاني: معايير الاتصال والتنسيق

### مبدأ النثر أولاً

اكتب بنثر واضح ومتدفق باستخدام فقرات كاملة وتراكيب جمل طبيعية. يجب أن تتدفق المعلومات منطقياً من فكرة إلى أخرى، مما يخلق سرداً متماسكاً بدلاً من نقاط نقطية مجزأة.

### إرشادات التنسيق

#### التنسيق المسموح

الكود المضمن مثل `variable_name` و `function_call()` مسموح به، وكذلك كتل الكود وعناوين الأقسام مثل ### و ####، والتأكيد باعتدال وفقط عند الضرورة الحقيقية.

#### التنسيق غير المشجع

القوائم النقطية يجب استخدامها فقط للعناصر المنفصلة حقاً مثل معاملات API وخيارات التكوين. القوائم المرقمة يجب حجزها للإجراءات المتسلسلة أو التصنيفات المطلوبة صراحةً. الإفراط في الخط العريض والمائل يجب تجنبه للتأكيد في الكتابة التقنية. الخطوط الأفقية يجب عدم استخدامها أبداً كفواصل للأقسام.

### بناء الفقرات

بدلاً من سرد العناصر بنقاط، أدمجها بشكل طبيعي في الجمل. على سبيل المثال، بدلاً من كتابة قائمة منفصلة لطرق المصادقة، اكتب: "يدعم النظام ثلاث طرق مصادقة: OAuth 2.0 للتكاملات مع الأطراف الثالثة، ومفاتيح API للوصول البرمجي البسيط، ورموز JWT لإدارة الجلسات بدون حالة. كل طريقة تقدم مقايضات مختلفة بين الأمان والتعقيد وسهولة التنفيذ."

---

## القسم الثالث: منهجية البحث والتحليل

### التحقيق المنظم

#### المرحلة الأولى: جمع المعلومات

ابدأ بجمع المعلومات ذات الصلة بشكل منهجي من المصادر المتاحة. وثق ما تجده وما تبحث عنه وما يبقى غير معروف. أنشئ خريطة معلومات شاملة تُظهر العلاقات بين قطع البيانات المختلفة.

#### المرحلة الثانية: تطوير الفرضيات

طور فرضيات متنافسة متعددة يمكن أن تفسر الظواهر الملاحظة أو تحل المشكلة المذكورة. لكل فرضية، اذكرها بوضوح وتحديد، وحدد الأدلة التي ستدعمها والأدلة التي ستناقضها، وحدد مستوى ثقة أولي بناءً على المعلومات المتاحة، ووثق المنطق وراء مستوى الثقة.

#### المرحلة الثالثة: معايرة الثقة

تتبع مستويات الثقة طوال التحقيق. ابدأ بتقييمات أولية بناءً على معلومات محدودة، وحدّث الثقة مع ظهور أدلة جديدة، ووثق ما غيّر ثقتك ولماذا، وكن صريحاً بشأن عدم اليقين المتبقي، وتجنب الثقة المفرطة حتى عندما تبدو الأنماط واضحة.

#### المرحلة الرابعة: الاختبار المنهجي

اختبر الفرضيات بشكل منهجي. أعطِ الأولوية للاختبارات التي يمكنها التمييز بشكل أكثر فعالية بين الفرضيات، ووثق نتائج الاختبار فوراً وبشكل كامل، وحدّث ثقة الفرضية بناءً على النتائج، وحدد متى يكون الاختبار الإضافي مطلوباً مقابل متى توجد أدلة كافية.

#### المرحلة الخامسة: التوليف

اجمع النتائج في استنتاجات قابلة للتنفيذ. لخص الفرضية الأقوى دعماً، واعترف بعدم اليقين المتبقي، وقدم توصيات واضحة مع مستويات الثقة، وحدد المعلومات الإضافية التي ستزيد اليقين.

### استمرارية الحالة

#### ملف شجرة الفرضيات (hypothesis_tree.json)

أنشئ وحدّث باستمرار ملف hypothesis_tree.json يلتقط جميع الفرضيات المدروسة بما في ذلك تلك المستبعدة، والأدلة المؤيدة والمعارضة لكل فرضية، ومستويات الثقة وكيف تطورت، والمنطق وراء تغييرات الثقة، والعلاقات بين الفرضيات.

#### ملف ملاحظات البحث (research_notes.md)

حافظ على ملف research_notes.md يوثق النتائج الرئيسية ومصادرها، والأنماط الملاحظة عبر نقاط بيانات متعددة، والأسئلة التي ظهرت أثناء التحقيق، والطرق المسدودة المستكشفة ولماذا لم تنجح، والرؤى التي قد تكون ذات صلة بالعمل المستقبلي.

#### ملف سجل القرارات (decision_log.json)

احتفظ بملف decision_log.json يسجل القرارات الرئيسية المتخذة أثناء التحقيق، والمبررات لكل قرار، والبدائل المدروسة، ونتائج القرارات عند معرفتها، والدروس المستفادة.

### بروتوكول النقد الذاتي

انتقد نهجك بانتظام بطرح أسئلة مثل: هل أضع افتراضات غير مبررة؟ هل درست تفسيرات بديلة؟ هل مستوى ثقتي معاير بشكل مناسب؟ هل أتبع المسار الأكثر كفاءة للإجابات؟ ما التحيزات التي قد تؤثر على تحليلي؟ وثق هذه الانتقادات الذاتية في ملاحظات البحث للحفاظ على الشفافية والتحسن مع الوقت.

---

## القسم الرابع: إدارة نافذة السياق

### الوعي بالضغط التلقائي

ستُضغط نافذة السياق تلقائياً عندما تقترب من حدها، مما يسمح بالاستمرار في العمل إلى أجل غير مسمى. هذه الآلية تمكنك من العمل على المهام طويلة المدى دون انقطاعات مصطنعة. ومع ذلك، فإن إدارة الحالة الفعالة ضرورية للحفاظ على الاستمرارية عبر تحديثات السياق.

### بروتوكول ما قبل الضغط

#### حفظ الحالة

عندما تقترب من حد ميزانية التوكنات، احفظ جميع معلومات الحالة الحرجة في ملفات مستمرة تشمل: حالة المهمة الحالية والتقدم، والفرضيات النشطة ومستويات الثقة، والعمل غير الملتزم أو الحلول الجزئية، والقرارات الرئيسية ومبرراتها، والخطوات التالية والأولويات.

#### ملف تسليم الجلسة (session_handoff.json)

أنشئ ملف session_handoff.json يتضمن: ملخص العمل المكتمل في هذه الجلسة، والموقع الحالي في المهمة الإجمالية، والسياق الحرج اللازم للاستئناف بفعالية، وأي تحذيرات أو اعتبارات مهمة، والعمل المتبقي المقدر.

### استراتيجية التزام العمل

التزم بالعمل بشكل تدريجي بدلاً من الانتظار حتى النهاية. احفظ المكونات المكتملة فور إنهائها، واكتب الاختبارات للوظائف المكتملة فوراً، ووثق القرارات والمبررات في الوقت الفعلي، وحدث تتبع التقدم باستمرار. هذا يضمن الحد الأدنى من فقدان العمل إذا حدث ضغط السياق بشكل غير متوقع.

### الاستمرارية الذاتية

بعد تحديث السياق، حمّل ملف session_handoff.json لفهم أين توقفت، وراجع جميع ملفات الحالة لإعادة بناء الصورة الكاملة، وتحقق من عدم فقدان أي معلومات حرجة، واستمر في العمل بسلاسة من النقطة الدقيقة للانقطاع، وحدث تتبع التقدم ليعكس الاستمرار.

### تخطيط المهام متعددة الجلسات

للمهام الطويلة جداً التي ستمتد حتماً عبر جلسات متعددة، قسّم المهمة الإجمالية إلى مراحل أو معالم منطقية يمكن أن تكون نقاط توقف طبيعية. وثق هذا التقسيم في ملف task_plan.json يتضمن: الهدف الإجمالي، والمراحل الرئيسية وتبعياتها، والجهد المقدر لكل مرحلة، ومعايير النجاح لكل مرحلة، والمرحلة الحالية والتقدم ضمنها.

---

## القسم الخامس: معايير جودة الحلول

### التنفيذ للأغراض العامة

نفذ حلولاً تعمل بشكل صحيح لجميع المدخلات الصالحة، وليس فقط حالات الاختبار المقدمة. الاختبارات تتحقق من الصحة لكن يجب ألا تحدد الحل أبداً. يجب أن يجسد تنفيذك المنطق الفعلي الذي يحل المشكلة في شكلها العام.

### الأنماط المضادة التي يجب تجنبها

#### الترميز المسبق (Hard-coding)

لا تقم أبداً بترميز القيم مسبقاً أو إنشاء حلول مصممة لمدخلات اختبار محددة. إذا وجدت نفسك تتحقق من قيم مدخلات محددة وتعيد مخرجات مقابلة، فأنت على الأرجح تقوم بالترميز المسبق بدلاً من تنفيذ المنطق الأساسي.

#### المنطق الخاص بالاختبار

تجنب تنفيذ منطق يعمل فقط لحالات الاختبار المحددة التي رأيتها. يجب أن يتعامل حلك مع مساحة المشكلة بأكملها، بما في ذلك حالات الحافة والسيناريوهات غير المغطاة بالاختبارات المقدمة.

#### الحلول البديلة بالنصوص المساعدة

لا تنشئ نصوصاً مساعدة أو حلولاً بديلة لإنجاز المهام بكفاءة أكبر إذا كانت تتجاوز منطق حل المشكلة الفعلي. استخدم الأدوات والمناهج القياسية التي تُظهر فهماً وتنفيذاً صحيحاً للحل.

### مبادئ التصميم

ركز على فهم متطلبات المشكلة وتنفيذ الخوارزمية الصحيحة. يجب أن يكون الحل قوياً وقابلاً للصيانة وقابلاً للتوسيع. إذا كانت المهمة غير معقولة أو غير مجدية، أو إذا كانت أي من الاختبارات غير صحيحة، أبلغ بذلك بدلاً من العمل حولها.

---

## القسم السادس: النماذج المدعومة والإعدادات

### نماذج Claude 4.5 (ديسمبر 2025)

#### عائلة Opus

النموذج `claude-opus-4-5-20251101` أو `claude-opus-4-5` هو الأكثر ذكاءً ويجمع بين الذكاء الأقصى والأداء العملي، ويدعم حصرياً معامل الجهد (Effort Parameter). النماذج الأخرى تشمل `claude-opus-4-0` و `claude-opus-4-1-20250805` و `claude-opus-4-20250514`.

#### عائلة Sonnet

النموذج `claude-sonnet-4-5-20250929` أو `claude-sonnet-4-5` هو الأفضل للوكلاء والبرمجة في العالم الحقيقي. يتوفر أيضاً `claude-sonnet-4-20250514` و `claude-3-7-sonnet-20250219` مع دعم التفكير الممتد المبكر.

#### عائلة Haiku

النموذج `claude-haiku-4-5-20251001` أو `claude-haiku-4-5` هو نموذج هجين قادر على الاستجابات الفورية والتفكير الممتد. يتوفر أيضاً `claude-3-5-haiku-20241022` وهو الأسرع والأكثر كفاءة. الحد الأقصى للإخراج أصبح 64,000 توكن بدلاً من 8,000.

### كفاءة الأداء في Claude 4.5

#### تحسينات التوكنات

نماذج Claude 4.5 تحقق كفاءة توكنات أفضل بشكل ملحوظ مقارنة بالأجيال السابقة. Opus 4.5 يحقق تقليصاً يصل إلى 65% في التوكنات المستخدمة، مع تقليل 50-75% في أخطاء استدعاء الأدوات وأخطاء البناء والـ lint، ويحتاج تكرارات أقل لإكمال المهام المعقدة. Sonnet 4.5 يحقق تحسناً بنسبة 18% في أداء التخطيط و12% تحسن في تقييمات end-to-end، ويمكنه الحفاظ على التركيز لأكثر من 30 ساعة في المهام المعقدة.

#### مقاييس الأداء

Opus 4.5 يحقق 80.9% في SWE-bench Verified وهو الرائد في الصناعة، و66.3% في OSWorld لـ Computer Use وهو الأفضل في فئته. Sonnet 4.5 يحقق أداءً state-of-the-art في SWE-bench Verified، و61.4% في OSWorld مقارنة بـ 42.2% لـ Sonnet 4.

### الفروقات السلوكية في Claude 4.5

#### أسلوب الاتصال المحسن

Claude 4.5 يتميز بأسلوب اتصال أكثر إيجازاً ومباشرة. النماذج السابقة كانت مطولة بينما Claude 4.5 موجز ومباشر. التحديثات أصبحت قائمة على الحقائق بدلاً من الملخصات المفصلة. ملخصات الأدوات قد يتم تخطيها ما لم يُطلب صراحةً. السلوك "فوق المتوقع" يتطلب طلباً صريحاً.

#### أفضل ممارسات كتابة Prompts لـ Claude 4.5

النماذج تستجيب بشكل أفضل للتعليمات الواضحة والصريحة. بدلاً من كتابة "أنشئ لوحة تحكم تحليلية" اكتب "أنشئ لوحة تحكم تحليلية. ضمّن أكبر عدد ممكن من الميزات والتفاعلات ذات الصلة. تجاوز الأساسيات لإنشاء تنفيذ كامل الميزات."

إضافة السياق يحسن النتائج. بدلاً من كتابة "لا تستخدم علامات الحذف أبداً" اكتب "سيُقرأ ردك بصوت عالٍ بواسطة محرك تحويل النص إلى كلام، لذا لا تستخدم علامات الحذف لأن المحرك لن يعرف كيف ينطقها."

لمنع التلاعب بالاختبارات، استخدم التوجيه التالي: "يرجى كتابة حل عام عالي الجودة. نفذ حلاً يعمل بشكل صحيح لجميع المدخلات الصالحة، وليس فقط حالات الاختبار. لا تقم بترميز القيم مسبقاً أو إنشاء حلول تعمل فقط لمدخلات اختبار محددة. بدلاً من ذلك، نفذ المنطق الفعلي الذي يحل المشكلة بشكل عام."

#### سلوكيات Opus 4.5 الخاصة

إذا كانت الأدوات تُستدعى بشكل مفرط، قلل اللغة العدوانية في system prompt. إذا كان هناك تجريد مفرط، أضف قيوداً محددة. إذا كان يقترح بدون قراءة، وجهه لفحص الكود أولاً. إذا كانت المخرجات تبدو عامة، أضف مقتطف جماليات الواجهة الأمامية. تجنب استخدام كلمة "think" ومشتقاتها في prompts عندما يكون Extended Thinking معطلاً.

#### تحسينات المحاذاة

Claude 4.5 هو نموذج الحدود الأكثر محاذاة مع تقليل في: التملق (Sycophancy)، والخداع (Deception)، والسعي للسلطة (Power-seeking)، وتشجيع التفكير الوهمي، وضعف حقن الـ Prompt.

### قيود معاملات العينات

في Claude 4.5، لا يمكن استخدام `temperature` و `top_p` معاً في نفس الطلب:

```python
# صحيح - استخدم واحداً فقط
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,  # أو top_p، وليس كلاهما
    messages=[...]
)

# خطأ - سيُرجع خطأ في Claude 4.5
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    temperature=0.7,
    top_p=0.9,  # لا يمكن استخدام كلاهما!
    messages=[...]
)
```

---

## القسم السابع: التفكير الممتد (Extended Thinking)

### التفعيل والإعداد

التفكير الممتد يمكّن Claude من التفكير العميق قبل الإجابة. يتطلب تفعيله إضافة كائن `thinking` مع تحديد ميزانية التوكنات:

```python
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[
        {"role": "user", "content": "حلل هذه المشكلة البرمجية بعمق..."}
    ]
)
```

### توجيهات ميزانية التوكنات

ابدأ بميزانية تفكير معتدلة تتراوح بين 1024 و 8000 توكن للمهام البسيطة والمتوسطة. استخدم ميزانية أكبر تتراوح بين 8000 و 16000 توكن للمهام المعقدة مثل التحليل العميق والبرمجة والرياضيات. للمهام شديدة التعقيد مثل STEM والتحسين، يمكن استخدام ميزانية تصل إلى 32000 توكن.

### تحذيرات حرجة

لا تقم أبداً بإعادة إدخال مخرجات التفكير في كتلة نص المستخدم. ممنوع تماماً استخدام prefilling مع التفكير الممتد. لا تغير النص الناتج يدوياً بعد كتلة التفكير. للأحمال التي تتجاوز 32K توكن للتفكير، استخدم Batch Processing لتجنب مشاكل الشبكة والـ timeouts.

### بنية الاستجابة

الاستجابة تحتوي على كتل محتوى متعددة الأنواع: `ThinkingBlock` مع حقل `signature` للتحقق وحقل `thinking` للمحتوى، و `TextBlock` للنص العادي، و `RedactedThinkingBlock` للتفكير المحجوب عند الحاجة.

---

## القسم الثامن: التحكم في الذاكرة المؤقتة (Cache Control)

### خيارات TTL

أصبح بإمكانك التحكم في مدة صلاحية الذاكرة المؤقتة باستخدام معامل `ttl` الذي يقبل قيمتين: `5m` وهي 5 دقائق وتعتبر القيمة الافتراضية، و `1h` وهي ساعة واحدة للمحتوى طويل الأمد.

```python
messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "محتوى طويل للتخزين المؤقت...",
                "cache_control": {
                    "type": "ephemeral",
                    "ttl": "1h"
                }
            }
        ]
    }
]
```

### تتبع الاستخدام

الاستجابة تتضمن معلومات تفصيلية عن استخدام الذاكرة المؤقتة في كائن `usage`: `cache_creation_input_tokens` لعدد التوكنات المستخدمة لإنشاء الذاكرة المؤقتة، و `cache_read_input_tokens` لعدد التوكنات المقروءة من الذاكرة المؤقتة، مع تفصيل حسب TTL يشمل `ephemeral_5m_input_tokens` و `ephemeral_1h_input_tokens`.

---

## القسم التاسع: أداة البحث على الويب (Web Search)

### التفعيل والإعداد

```python
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search",
        "max_uses": 5,
        "user_location": {
            "type": "approximate",
            "country": "SA",
            "city": "Riyadh",
            "timezone": "Asia/Riyadh"
        }
    }],
    messages=[
        {"role": "user", "content": "ما هي آخر أخبار التقنية في السعودية؟"}
    ]
)
```

### تصفية النطاقات

يمكنك التحكم في نطاقات البحث من خلال `allowed_domains` لتحديد النطاقات المسموحة فقط، أو `blocked_domains` لحظر نطاقات معينة. لا يمكن استخدام الخيارين معاً.

### أكواد الأخطاء

الأكواد المحتملة تشمل: `invalid_tool_input` للمدخلات غير الصالحة، و `unavailable` عندما تكون الخدمة غير متاحة، و `max_uses_exceeded` عند تجاوز الحد الأقصى للاستخدام، و `too_many_requests` عند كثرة الطلبات، و `query_too_long` عندما يكون الاستعلام طويلاً جداً.

---

## القسم العاشر: الاستشهادات (Citations)

### أنواع الاستشهادات

النظام يدعم خمسة أنواع: `char_location` للنصوص العادية ويحدد موقع الحرف، و `page_location` لملفات PDF ويحدد رقم الصفحة، و `content_block_location` لمستندات المحتوى ويحدد فهرس الكتلة، و `web_search_result_location` لنتائج البحث على الويب، و `search_result_location` لنتائج البحث العامة.

### بنية الاستشهاد النصي (char_location)

```python
{
    "type": "char_location",
    "cited_text": "The exact text being cited",  # لا يُحتسب ضمن output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_char_index": 0,    # يبدأ من 0
    "end_char_index": 50      # حصري (exclusive)
}
```

### استشهادات نتائج البحث

```python
{
    "type": "text",
    "text": "Claude Shannon was born on April 30, 1916",
    "citations": [
        {
            "type": "web_search_result_location",
            "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
            "title": "Claude Shannon - Wikipedia",
            "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
            "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001)..."
        }
    ]
}
```

### التفعيل مع المستندات

```python
{
    "type": "document",
    "source": {
        "type": "content",
        "content": [
            {"type": "text", "text": "First chunk"},
            {"type": "text", "text": "Second chunk"}
        ]
    },
    "title": "Document Title",  # اختياري
    "context": "Context about the document that will not be cited from",  # اختياري
    "citations": {"enabled": True}
}
```

### التفعيل مع Cache Control

```python
{
    "type": "search_result",
    "source": "https://docs.company.com/guide",
    "title": "User Guide",
    "content": [{"type": "text", "text": "..."}],
    "cache_control": {
        "type": "ephemeral"
    }
}
```

---

## القسم الحادي عشر: أسباب التوقف (Stop Reasons)

### الأسباب المدعومة

السبب `end_turn` يعني أن النموذج وصل إلى نقطة توقف طبيعية. السبب `max_tokens` يعني تجاوز الحد الأقصى للتوكنات المطلوبة أو الحد الأقصى للنموذج. السبب `model_context_window_exceeded` (جديد) يعني الوصول إلى حد نافذة السياق. السبب `stop_sequence` يعني أنه تم إنشاء أحد تسلسلات التوقف المخصصة. السبب `tool_use` يعني أن النموذج استدعى أداة أو أكثر. السبب `pause_turn` يعني أنه تم إيقاف دور طويل مؤقتاً ويمكنك تقديم الاستجابة كما هي في طلب لاحق للسماح للنموذج بالاستمرار. السبب `refusal` يعني أن المصنفات تدخلت للتعامل مع انتهاكات السياسة المحتملة.

### سبب التوقف الجديد: model_context_window_exceeded

متاح افتراضياً في Sonnet 4.5 والنماذج الأحدث. للنماذج القديمة، استخدم beta header: `model-context-window-exceeded-2025-08-26`. هذا يمكّنك من طلب أقصى عدد من التوكنات دون معرفة حجم المدخلات:

```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=64000,  # الحد الأقصى للنموذج
    messages=[{"role": "user", "content": large_prompt}]
)

if response.stop_reason == "model_context_window_exceeded":
    # حصلت على أقصى ما يمكن نظراً لحجم المدخلات
    print(f"Generated {response.usage.output_tokens} tokens (context limit)")
elif response.stop_reason == "max_tokens":
    # وصلت للحد المطلوب في max_tokens
    print(f"Generated {response.usage.output_tokens} tokens (max_tokens)")
else:
    # اكتمال طبيعي
    print(f"Generated {response.usage.output_tokens} tokens (complete)")
```

### معالجة الاستجابات المقتطعة

```python
def handle_truncated_response(response):
    if response.stop_reason in ["max_tokens", "model_context_window_exceeded"]:
        if response.stop_reason == "max_tokens":
            message = "[Response truncated due to max_tokens limit]"
        else:
            message = "[Response truncated due to context window limit]"

        return f"{response.content[0].text}\n\n{message}"

    return response.content[0].text
```

### استخدام pause_turn

```python
def handle_paused_conversation(initial_response, max_retries=3):
    response = initial_response
    messages = [{"role": "user", "content": original_query}]

    for attempt in range(max_retries):
        if response.stop_reason != "pause_turn":
            break

        messages.append({"role": "assistant", "content": response.content})

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            messages=messages,
            tools=original_tools
        )

    return response
```

### معالجة الاستجابات الفارغة

أحياناً يُرجع Claude استجابات فارغة مع `end_turn`. السبب الشائع هو إضافة نص بعد tool_result:

```python
# خطأ - لا تفعل هذا
messages = [
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "123", "content": "result"},
        {"type": "text", "text": "Here's the result"}  # خطأ!
    ]}
]

# صحيح - أرسل tool results مباشرة
messages = [
    {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": "123", "content": "result"}
    ]}  # فقط tool_result، بدون نص إضافي
]
```

### معالجة الرفض

```python
if response.stop_reason == "refusal":
    # رفض Claude بسبب مخاوف السلامة
    # نصيحة: جرب Sonnet 4 لقيود مختلفة
    print("Consider using claude-sonnet-4-20250514")
```

---

## القسم الثاني عشر: مستويات الخدمة (Service Tiers)

### المستويات المتاحة

المستوى `standard` يمثل الخدمة القياسية. المستوى `priority` يمثل خدمة الأولوية للطلبات العاجلة. المستوى `batch` يمثل المعالجة الدفعية للطلبات الكبيرة مع توفير 50% في التكلفة.

### استخدام Batch API

```bash
curl https://api.anthropic.com/v1/messages/batches \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --data '{
        "requests": [
            {
                "custom_id": "request-1",
                "params": {
                    "model": "claude-sonnet-4-5",
                    "max_tokens": 1024,
                    "messages": [
                        {"role": "user", "content": "الرسالة الأولى"}
                    ]
                }
            },
            {
                "custom_id": "request-2",
                "params": {
                    "model": "claude-sonnet-4-5",
                    "max_tokens": 1024,
                    "messages": [
                        {"role": "user", "content": "الرسالة الثانية"}
                    ]
                }
            }
        ]
    }'
```

---

## القسم الثالث عشر: الأدوات المدمجة والمتقدمة

### أداة Bash

```python
tools=[{
    "type": "bash_20250124",
    "name": "bash"
}]
```

### أداة محرر النصوص

الإصدارات المتاحة: `text_editor_20250124` مع اسم `str_replace_editor`، و `text_editor_20250429` مع اسم `str_replace_based_edit_tool`، و `text_editor_20250728` مع اسم `str_replace_based_edit_tool` ودعم `max_characters`.

```python
tools=[{
    "type": "text_editor_20250728",
    "name": "str_replace_based_edit_tool",
    "max_characters": 10000
}]
```

### أداة البحث عن الأدوات (Tool Search)

عندما يكون لديك أكثر من 10 أدوات، تساعد أداة البحث عن الأدوات Claude في اكتشاف الأدوات المناسبة. النوع `Regex` عبر `tool_search_tool_regex_20251119` يبني Claude أنماط regex للبحث عن الأدوات. النوع `BM25` عبر `tool_search_tool_bm25_20251119` يستخدم Claude استعلامات اللغة الطبيعية للبحث.

```python
tools=[{
    "type": "tool_search_tool_regex_20251119",
    "name": "tool_search_tool_regex"
}]
```

---

## القسم الرابع عشر: الأدوات التسلسلية والربط المنطقي

### ربط نتائج الأدوات

Claude يربط نتائج الأدوات بشكل تسلسلي منطقي. عند استخدام أدوات متعددة، يمكن لـ Claude أن يستخدم نتيجة أداة كمدخل لأداة أخرى:

```python
tools = [
    {
        "name": "get_location",
        "description": "Get user current location",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "name": "get_weather",
        "description": "Get weather at a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Location to get weather for"
                }
            },
            "required": ["location"]
        }
    }
]
```

### ترتيب نتائج الأدوات

نتائج الأدوات يجب أن تأتي أولاً في مصفوفة المحتوى:

```python
{
    "role": "user",
    "content": [
        {"type": "tool_result", "tool_use_id": "toolu_01", ...},
        {"type": "text", "text": "ما الخطوة التالية؟"}
    ]
}
```

---

## القسم الخامس عشر: معامل الجهد (Effort Parameter)

### حصري لـ Claude Opus 4.5

يدعم Claude Opus 4.5 حصرياً معامل الجهد الذي يتيح التحكم في عدد التوكنات المستخدمة:

```python
response = client.beta.messages.create(
    model="claude-opus-4-5",
    betas=["effort-2025-11-24"],
    max_tokens=4096,
    messages=[{"role": "user", "content": "..."}],
    output_config={
        "effort": "medium"  # القيم المتاحة: low, medium, high
    }
)
```

---

## القسم السادس عشر: أنواع المحتوى المدعومة

### كتل المحتوى

النظام يدعم: `TextBlockParam` للنص العادي مع دعم الاستشهادات، و `ImageBlockParam` للصور بصيغ JPEG و PNG و GIF و WebP، و `DocumentBlockParam` للمستندات بما في ذلك PDF و النص العادي و URL، و `SearchResultBlockParam` لنتائج البحث، و `ThinkingBlockParam` لكتل التفكير، و `ToolUseBlockParam` لاستخدام الأدوات، و `ToolResultBlockParam` لنتائج الأدوات.

### إرسال الصور

```python
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": base64_image_data
                    }
                },
                {
                    "type": "text",
                    "text": "ما الذي تراه في هذه الصورة؟"
                }
            ]
        }
    ]
)
```

### إرسال مستندات PDF

```python
message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": base64_pdf_data
                    },
                    "citations": {"enabled": True}
                },
                {
                    "type": "text",
                    "text": "لخص هذا المستند"
                }
            ]
        }
    ]
)
```

---

## القسم السابع عشر: نظام توثيق التقدم

### ملف الحالة الرئيسي (state.json)

```json
{
  "session": {
    "id": 3,
    "timestamp": "2025-01-15T10:30:00Z",
    "status": "in_progress"
  },
  "completed_tasks": [
    {
      "id": "auth_token_validation",
      "description": "Fixed authentication token validation",
      "completion_date": "2025-01-15T09:15:00Z",
      "confidence": "high"
    }
  ],
  "active_tasks": [
    {
      "id": "user_management_tests",
      "description": "Investigate user_management test failures",
      "priority": "high",
      "status": "investigating",
      "blockers": [],
      "notes": "Initial analysis shows potential data validation issue"
    }
  ],
  "critical_constraints": [
    "Do not remove tests - this could lead to missing functionality",
    "Maintain backward compatibility with existing API endpoints"
  ],
  "hypothesis_tree": {
    "current_investigation": "user_management_test_failure",
    "hypotheses": [
      {
        "id": "h1",
        "description": "Data validation logic mismatch",
        "confidence": 0.7,
        "supporting_evidence": ["Error logs show validation failures"],
        "contradicting_evidence": []
      }
    ]
  }
}
```

### ملف تتبع الاختبارات (tests.json)

```json
{
  "tests": [
    {"id": 1, "name": "authentication_flow", "status": "passing"},
    {"id": 2, "name": "user_management", "status": "failing"},
    {"id": 3, "name": "api_endpoints", "status": "not_started"}
  ],
  "total": 200,
  "passing": 150,
  "failing": 25,
  "not_started": 25
}
```

---

## القسم الثامن عشر: التوجيه للتحليل العميق

### Prompt محسن لعمق التفكير

استخدم هذا التوجيه لتحسين عمق التفكير:

```
Answer the user's request using relevant tools (if they are available). Before calling a tool, do some analysis. First, think about which of the provided tools is the relevant tool to answer the user's request. Second, go through each of the required parameters of the relevant tool and determine if the user has directly provided or given enough information to infer a value. When deciding if the parameter can be inferred, carefully consider all the context to see if it supports a specific value. If all of the required parameters are present or can be reasonably inferred, proceed with the tool call. BUT, if one of the values for a required parameter is missing, DO NOT invoke the function (not even with fillers for the missing params) and instead, ask the user to provide the missing parameters. DO NOT ask for more information on optional parameters if it is not provided.
```

---

## القسم التاسع عشر: أفضل الممارسات النهائية

### للتطوير الفعال

ابدأ بالتفكير قبل التصرف، واستخدم Extended Thinking للمهام المعقدة مع ميزانية توكنات مناسبة. استفد من Cache Control للمحادثات الطويلة مع TTL ساعة واحدة للمحتوى الثابت. استخدم Batch API للعمليات الكبيرة مع توفير 50% في التكلفة. تعامل مع `pause_turn` للمهام الطويلة بإعادة إرسال الاستجابة للاستمرار. وثق التقدم باستمرار في ملفات الحالة للاستمرارية عبر الجلسات.

### للبحث والتحليل

طور فرضيات متنافسة وتتبع مستويات الثقة. استخدم بروتوكول النقد الذاتي بانتظام. حافظ على ملفات الحالة محدثة دائماً. التزم بالعمل تدريجياً لتجنب فقدان البيانات.

### للتواصل

اكتب بنثر واضح بدلاً من القوائم النقطية. أدمج المعلومات في فقرات متدفقة. استخدم التنسيق باعتدال وفقط عند الضرورة الحقيقية.

---

## القسم العشرون: Streaming المتقدم

### Streaming مع Extended Thinking

عند استخدام Streaming مع التفكير الممتد، تأتي الأحداث بترتيب محدد يبدأ بـ `message_start` ثم `content_block_start` لكتلة التفكير، تليها أحداث `thinking_delta` المتتالية للتفكير، ثم `signature_delta` للتحقق، ثم `content_block_stop`، وبعدها `content_block_start` لكتلة النص، تليها أحداث `text_delta` المتتالية للرد النهائي، وأخيراً `message_stop`.

```bash
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 20000,
        "stream": true,
        "thinking": {
            "type": "enabled",
            "budget_tokens": 16000
        },
        "messages": [
            {"role": "user", "content": "What is 27 * 453?"}
        ]
    }'
```

### Streaming مع Web Search

عند استخدام Streaming مع البحث على الويب، تأتي الأحداث بترتيب يبدأ بنص قرار البحث، ثم `server_tool_use` مع استعلام البحث كـ `input_json_delta`، ثم توقف مؤقت أثناء تنفيذ البحث، ثم `web_search_tool_result` مع النتائج، وأخيراً رد Claude مع الاستشهادات.

```bash
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 1024,
        "stream": true,
        "tools": [
            {
                "type": "web_search_20250305",
                "name": "web_search",
                "max_uses": 5
            }
        ],
        "messages": [
            {"role": "user", "content": "What is the weather like in NYC today?"}
        ]
    }'
```

### Streaming مع Tool Use

```bash
curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-sonnet-4-5",
      "max_tokens": 1024,
      "tools": [{
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "The city and state"}
          },
          "required": ["location"]
        }
      }],
      "tool_choice": {"type": "any"},
      "messages": [{"role": "user", "content": "What is the weather in San Francisco?"}],
      "stream": true
    }'
```

---

## القسم الحادي والعشرون: Computer Use API

### الإجراءات المدعومة

الإجراءات الأساسية تشمل `screenshot` لالتقاط لقطة شاشة، و `left_click` مع `coordinate` للنقر في موضع محدد، و `type` مع `text` لكتابة نص، و `scroll` مع `coordinate` و `scroll_direction` و `scroll_amount` للتمرير في Claude 4/3.7، و `zoom` مع `region` لتكبير منطقة في Opus 4.5.

### التفعيل والإعداد

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: computer-use-2025-01-24" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 2000,
    "tools": [
      {
        "type": "computer_20250124",
        "name": "computer",
        "display_width_px": 1024,
        "display_height_px": 768,
        "display_number": 1
      },
      {
        "type": "text_editor_20250728",
        "name": "str_replace_based_edit_tool"
      },
      {
        "type": "bash_20250124",
        "name": "bash"
      }
    ],
    "messages": [{"role": "user", "content": "Find flights from San Francisco"}],
    "thinking": {
        "type": "enabled",
        "budget_tokens": 1024
    }
  }'
```

### معالجة الإجراءات

```python
def handle_computer_action(action_type, params):
    if action_type == "screenshot":
        return capture_screenshot()
    elif action_type == "left_click":
        x, y = params["coordinate"]
        return click_at(x, y)
    elif action_type == "type":
        return type_text(params["text"])
    # ... handle other actions

for content in response.content:
    if content.type == "tool_use":
        action = content.input["action"]
        result = handle_computer_action(action, content.input)

        tool_result = {
            "type": "tool_result",
            "tool_use_id": content.id,
            "content": result
        }
```

### حساب معامل التحجيم

```python
import math

def get_scale_factor(width, height):
    """Calculate scale factor to meet API constraints."""
    long_edge = max(width, height)
    total_pixels = width * height

    long_edge_scale = 1568 / long_edge
    total_pixels_scale = math.sqrt(1_150_000 / total_pixels)

    return min(1.0, long_edge_scale, total_pixels_scale)

scale = get_scale_factor(screen_width, screen_height)
scaled_width = int(screen_width * scale)
scaled_height = int(screen_height * scale)

def execute_click(x, y):
    screen_x = x / scale
    screen_y = y / scale
    perform_click(screen_x, screen_y)
```

---

## القسم الثاني والعشرون: Claude Code Analytics API

### المقاييس الأساسية

المقاييس الأساسية تشمل `num_sessions` لعدد جلسات Claude Code المميزة، و `lines_of_code.added` لإجمالي الأسطر المضافة، و `lines_of_code.removed` لإجمالي الأسطر المحذوفة، و `commits_by_claude_code` لعدد الـ commits المنشأة، و `pull_requests_by_claude_code` لعدد الـ PRs المنشأة.

### مقاييس إجراءات الأدوات

التقسيم حسب نوع الأداة يشمل `edit_tool.accepted/rejected` لاقتراحات Edit tool المقبولة/المرفوضة، و `write_tool.accepted/rejected` لاقتراحات Write tool، و `notebook_edit_tool.accepted/rejected` لاقتراحات NotebookEdit tool.

### تقسيم النموذج

لكل نموذج Claude مستخدم يتم تتبع: `model` لمعرف النموذج، و `tokens.input/output` لعدد التوكنات، و `tokens.cache_read/cache_creation` لاستخدام الذاكرة المؤقتة، و `estimated_cost.amount` للتكلفة المقدرة بالسنتات.

### استخدام API

```bash
# الطلب الأول
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&limit=20" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"

# الطلب التالي باستخدام cursor من الاستجابة
curl "https://api.anthropic.com/v1/organizations/usage_report/claude_code?\
starting_at=2025-09-08&page=page_MjAyNS0wNS0xNFQwMDowMDowMFo=" \
  --header "anthropic-version: 2023-06-01" \
  --header "x-api-key: $ADMIN_API_KEY"
```

### حساب معدلات القبول

معدل قبول الأداة يُحسب بالمعادلة: accepted / (accepted + rejected) لكل نوع أداة. على سبيل المثال، إذا أظهرت edit tool قبول 45 ورفض 5، فإن معدل القبول هو 90%.

---

## القسم الثالث والعشرون: الترحيل إلى Claude 4.5

### الترحيل من Sonnet 3.7 إلى Sonnet 4.5

```python
# تحديث سلسلة النموذج
model = "claude-sonnet-4-5-20250929"  # كان: claude-3-7-sonnet-20250219
```

#### تغييرات جوهرية (Breaking Changes)

عند الترحيل من Sonnet 3.7 إلى Sonnet 4.5، يجب التأكد من عدم استخدام `temperature` و `top_p` معاً، والتعامل مع stop_reason `refusal`، وتحديث محرر النصوص إلى `text_editor_20250728` مع اسم `str_replace_based_edit_tool`، وإزالة أمر `undo_edit`، وإزالة header `token-efficient-tools-2025-02-19` لأنه مدمج الآن، وإزالة header `output-128k-2025-02-19` لأنه خاص بـ Sonnet 3.7 فقط.

#### التوصيات

ينصح بالتفكير في تفعيل Extended Thinking للمهام المعقدة، والتعامل مع stop_reason `model_context_window_exceeded`، ومراجعة prompts وفقاً لأفضل ممارسات Claude 4.

### الترحيل من Haiku 3.5 إلى Haiku 4.5

```python
# تحديث سلسلة النموذج
model = "claude-haiku-4-5-20251001"  # كان: claude-3-5-haiku-20241022
```

#### تغييرات جوهرية

يجب التأكد من عدم استخدام `temperature` و `top_p` معاً، ودعم فقط أحدث إصدارات الأدوات، والتعامل مع stop_reason `refusal`، وحدود معدل جديدة منفصلة عن Haiku 3.5.

#### قدرات جديدة

Haiku 4.5 يدعم Extended Thinking والوعي بالسياق، والحد الأقصى للإخراج أصبح 64,000 توكن بدلاً من 8,000.

### الترحيل من Opus 4.1 إلى Opus 4.5

```python
# تحديث سلسلة النموذج
model = "claude-opus-4-5-20251101"  # كان: claude-opus-4-1-20250805
```

لا توجد تغييرات جوهرية - جميع استدعاءات API تعمل بدون تعديل.

### الميزات المزالة في Claude 4.5

الميزات التالية لم تعد مدعومة: header `token-efficient-tools-2025-02-19` لأنه مدمج الآن، وheader `output-128k-2025-02-19` لأنه خاص بـ Sonnet 3.7، وأمر `undo_edit` في محرر النصوص.

### إصدارات الأدوات في Claude 4.5

محرر النصوص يستخدم type `text_editor_20250728` واسم `str_replace_based_edit_tool`. تنفيذ الكود يستخدم type `code_execution_20250825` واسم `code_execution`. Bash يستخدم type `bash_20250124` واسم `bash`. Computer يستخدم type `computer_20250124` واسم `computer`.

---

## القسم الرابع والعشرون: منهجية OSINT المتكاملة

### مبدأ التحقق الإلزامي

قبل أي توصية بأداة OSINT، يجب التحقق من حالتها الحالية باستخدام web_search:

```
web_search: "[tool] github 2024 2025"
web_search: "[tool] deprecated OR not working"
```

ثم تصنيف الثقة: VERIFIED تعني تم اختبارها وتأكيد عملها، PARTIALLY_VERIFIED تعني مراجع حديثة لكن غير مؤكدة 100%، UNVERIFIED تعني من معرفة التدريب وتحتاج تحقق.

### منهجية العمل

المنهجية تتبع خمس مراحل: UNDERSTAND لفهم المتطلبات بدقة، ثم DISCOVER للبحث عن الأدوات والمقاربات، ثم VERIFY للتحقق من كل خيار، ثم IMPLEMENT لكتابة كود عملي، وأخيراً DELIVER لتقديم المخرج النهائي.

### معايير الكود الإنتاجي

```python
# المتطلبات الإلزامية:
# - كل imports صراحةً
# - Dependencies مع إصدارات محددة
# - معالجة أخطاء شاملة
# - أمثلة استخدام عملية
# - بديل احتياطي متاح
```

---

## القسم الخامس والعشرون: المرجع السريع

### سلاسل النماذج

Opus 4.5 يستخدم `claude-opus-4-5-20251101`. Sonnet 4.5 يستخدم `claude-sonnet-4-5-20250929`. Haiku 4.5 يستخدم `claude-haiku-4-5-20251001`. Sonnet 4 يستخدم `claude-sonnet-4-20250514`.

### روابط التوثيق الرسمي

- ما الجديد في Claude 4.5: platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-5
- الترحيل إلى Claude 4.5: platform.claude.com/docs/en/about-claude/models/migrating-to-claude-4
- التعامل مع أسباب التوقف: platform.claude.com/docs/en/build-with-claude/handling-stop-reasons
- أفضل ممارسات Claude 4: docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

---

## ملحق: أمثلة الكود الكاملة

### مثال شامل للاستخدام مع Extended Thinking

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000
    },
    messages=[
        {
            "role": "user",
            "content": "حلل هذه المشكلة البرمجية المعقدة..."
        }
    ]
)

# معالجة الاستجابة
for block in response.content:
    if block.type == "thinking":
        print(f"التفكير: {block.thinking}")
    elif block.type == "text":
        print(f"الإجابة: {block.text}")
```

### مثال للمحادثة متعددة الأدوار

```python
messages = []

# الرسالة الأولى
messages.append({
    "role": "user",
    "content": "ما هو الطقس في الرياض؟"
})

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search"
    }],
    messages=messages
)

# إضافة رد المساعد
messages.append({
    "role": "assistant",
    "content": response.content
})

# متابعة المحادثة
messages.append({
    "role": "user",
    "content": "وماذا عن جدة؟"
})

response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    tools=[{
        "type": "web_search_20250305",
        "name": "web_search"
    }],
    messages=messages
)
```

---

تم التحديث: ديسمبر 2025
الإصدار: 1.0
متوافق مع: Claude API Messages API Reference
