"""Evaluation prompts for different data types (Chinese and English versions)."""


# ==================== TYPE 1: Single-Step UI Transitions ====================

TYPE1_EVAL_PROMPT = """⚠️ BLIND EVALUATION MODE
- The model identity is anonymized. Do NOT infer quality from names.
- Evaluate SOLELY based on visual evidence and the provided text descriptions.

You are an EXTREMELY HARSH, UNCOMPROMISING GUI CHANGE EVALUATION EXPERT. Score ONLY by visual evidence. High scores (4-5) require near-perfect evidence.

You will receive:
- Initial Image: the UI state BEFORE the operation
- Generated Image: the model's predicted UI state AFTER the operation
- Caption: a natural language description of what changed / what should happen

Score 5 dimensions (0-5 integers, EXTREMELY STRICT):

**goal** (Goal Achievement): Does the generated state achieve the caption-described change?
- 5: Caption change is achieved completely and unambiguously. All key elements mentioned in the caption are present and correctly transformed. No ambiguity about whether the change matches the description.
- 4: Goal is achieved with only minor, non-critical omissions or formatting differences. The core change is clearly visible and matches the caption, but there might be slight differences in layout, text formatting, or minor elements not central to the goal.
- 3: Goal is mostly achieved but key details are ambiguous/partially missing. The main intent is recognizable, but important elements are unclear, partially implemented, or require inference to confirm they match the caption.
- 2: Partial achievement; only a small portion of the intended change is visible. Most of the expected transformation is missing or incorrect, though some elements loosely relate to the caption.
- 1: Barely related; the change does not match caption semantics. There might be a superficial similarity, but the core change described in the caption is not present.
- 0: Complete failure; no relevant change or totally wrong change. The generated image shows either no change from the initial state or a change completely unrelated to the caption.

**logic** (Interaction/State Logic): Is the change consistent with plausible GUI interaction and state transitions?
- 5: Transitions are fully plausible and consistent with standard UI behavior. The change follows natural GUI interaction patterns, state transitions are logical, and there are no impossible jumps or discontinuities. The transformation looks like a real UI would behave.
- 4: Mostly plausible; minor implausibility but still credible. The overall transition makes sense, but there might be slight inconsistencies that don't break the believability of the interaction.
- 3: Some implausible elements; still partially coherent. The change shows recognizable UI logic in parts, but contains elements that don't follow standard interaction patterns.
- 2: Largely implausible; broken state transition or inconsistent UI behavior. The change shows significant logical problems.
- 1: Almost entirely illogical; UI changes contradict basic interaction patterns. The transformation violates fundamental UI principles.
- 0: Impossible; severe "teleportation" or nonsensical transformation.

**consistency** (Preservation): Are unrelated regions preserved from the Initial Image?
- 5: Unaffected regions are preserved nearly perfectly. Every pixel outside the directly affected area is identical between Initial and Generated images.
- 4: Minor drift (small shifts, slight color/blur changes) but clearly preserved.
- 3: Noticeable drift in multiple areas, but the overall UI identity is maintained.
- 2: Significant unintended changes outside the target region.
- 1: Widespread unintended changes; most of the UI is altered.
- 0: Entire screen is corrupted or replaced.

**ui** (UI Plausibility/Integrity): Are UI elements plausible (no hallucinations, broken layout)?
- 5: UI components are coherent, correctly structured, and look native. All elements follow platform conventions.
- 4: Mostly coherent; minor layout/element issues.
- 3: Several element/layout issues but still resembles a usable UI.
- 2: Many hallucinations or severe layout problems.
- 1: UI is mostly broken; elements are nonsensical.
- 0: UI is unusable or completely hallucinated.

**quality** (Visual Quality): Visual readability (text/icon clarity, artifacts).
- 5: Crisp, readable, no obvious artifacts.
- 4: Very readable; minor blur/artifacts.
- 3: Readable but noticeable blur/artifacts in important areas.
- 2: Significant quality degradation; text/icons hard to read.
- 1: Severe artifacts; most text is unreadable.
- 0: Completely unusable image quality.

Essential Rules:
- Judge ONLY by visual evidence and the provided caption
- DO NOT invent or assume details not visible in images
- Be EXTREMELY conservative with high scores (4-5 require ironclad evidence)
- Justifications must be concise (≤2 sentences) and cite concrete observations
- If uncertain, assign lower score

Output ONLY JSON:
{
  "goal": {"s": <0-5>, "j": "<justification>"},
  "logic": {"s": <0-5>, "j": "<justification>"},
  "consistency": {"s": <0-5>, "j": "<justification>"},
  "ui": {"s": <0-5>, "j": "<justification>"},
  "quality": {"s": <0-5>, "j": "<justification>"}
}
"""


TYPE2_EVAL_PROMPT = """You are a GUI trajectory evaluation expert. Evaluate a 6-frame UI trajectory sequence.

You will receive:
- Frame 0: Initial state (reference)
- Frames 1-5: Generated sequence showing task progression

Evaluate across 5 dimensions (0-5):

**task_completion**: Does Frame 5 show achievement of the stated goal?
**interaction_logic**: Are transitions between frames logical and coherent?
**visual_consistency**: Do UI elements remain stable across frames (no jitter, corruption)?
**element_integrity**: Are UI elements native-looking (no hallucinations, impossible states)?
**visual_quality**: Are images clear (good text readability, minimal artifacts)?

Scoring rubric: 5=Perfect, 4=Minor issues, 3=Moderate issues, 2=Significant problems, 1=Severe issues, 0=Complete failure

Output ONLY JSON:
{
  "task_completion": {"s": <0-5>, "j": "<brief justification>"},
  "interaction_logic": {"s": <0-5>, "j": "<brief justification>"},
  "visual_consistency": {"s": <0-5>, "j": "<brief justification>"},
  "element_integrity": {"s": <0-5>, "j": "<brief justification>"},
  "visual_quality": {"s": <0-5>, "j": "<brief justification>"}
}
"""


TYPE5_EVAL_PROMPT = """You are a grounding/spatial task evaluation expert.

Evaluate whether the generated UI correctly implements the grounding task specified in the instruction.

Dimensions:
- **location_accuracy**: Are spatial references from the instruction correctly represented?
- **interaction_logic**: Does the UI show logical state for the specified task?
- **element_integrity**: Are UI elements plausible and native-looking?
- **visual_quality**: Is the image clear and readable?
- **instruction_adherence**: Does the overall output match the given instruction?

Each dimension: 0-5 scale

Output ONLY JSON:
{
  "location_accuracy": {"s": <0-5>, "j": "<justification>"},
  "interaction_logic": {"s": <0-5>, "j": "<justification>"},
  "element_integrity": {"s": <0-5>, "j": "<justification>"},
  "visual_quality": {"s": <0-5>, "j": "<justification>"},
  "instruction_adherence": {"s": <0-5>, "j": "<justification>"}
}
"""


TYPE3_EVAL_PROMPT = """You are a fictional app trajectory evaluation expert.

Evaluate a multi-frame UI trajectory sequence based on:
- Instruction: The user's natural language instruction/goal
- Generated frames: Model's predicted UI progression

Evaluate across 5 dimensions (0-5):

**trajectory_text_alignment**: Does the sequence follow the instruction trajectory?
**interaction_logic**: Are transitions between frames logical and coherent?
**visual_consistency**: Do UI elements remain stable across frames?
**element_integrity**: Are UI elements native-looking (no hallucinations)?
**visual_quality**: Are images clear with good text readability?

Scoring: 5=Perfect, 4=Minor issues, 3=Moderate, 2=Significant problems, 1=Severe, 0=Complete failure

Output ONLY JSON:
{
  "trajectory_text_alignment": {"s": <0-5>, "j": "<brief justification>"},
  "interaction_logic": {"s": <0-5>, "j": "<brief justification>"},
  "visual_consistency": {"s": <0-5>, "j": "<brief justification>"},
  "element_integrity": {"s": <0-5>, "j": "<brief justification>"},
  "visual_quality": {"s": <0-5>, "j": "<brief justification>"}
}
"""


TYPE4_EVAL_PROMPT = """You are a real app trajectory evaluation expert.

Evaluate a multi-frame UI trajectory sequence showing real app interactions:
- Instruction: The user's natural language instruction/goal
- Generated frames: Model's predicted UI progression for real apps

Evaluate across 5 dimensions (0-5):

**trajectory_text_alignment**: Does the sequence follow the instruction trajectory?
**interaction_logic**: Are transitions between frames logical and coherent?
**visual_consistency**: Do UI elements remain stable across frames?
**element_integrity**: Are UI elements native-looking (no hallucinations)?
**visual_quality**: Are images clear with good text readability?

Scoring: 5=Perfect, 4=Minor issues, 3=Moderate, 2=Significant problems, 1=Severe, 0=Complete failure

Output ONLY JSON:
{
  "trajectory_text_alignment": {"s": <0-5>, "j": "<brief justification>"},
  "interaction_logic": {"s": <0-5>, "j": "<brief justification>"},
  "visual_consistency": {"s": <0-5>, "j": "<brief justification>"},
  "element_integrity": {"s": <0-5>, "j": "<brief justification>"},
  "visual_quality": {"s": <0-5>, "j": "<brief justification>"}
}
"""


# ==================== CHINESE VERSIONS ====================

TYPE1_EVAL_PROMPT_ZH = """⚠️ 盲评模式
- 模型身份已匿名，请勿根据名称推断质量
- 仅基于视觉证据和提供的文字描述进行评估

你是一位极其严苛的 GUI 变化评估专家。仅根据视觉证据给出评分，高分（4-5）需要近乎完美的证据。

你将收到：
- 初始图像：操作前的 UI 状态
- 生成图像：模型预测的操作后 UI 状态
- 文字描述：自然语言描述变化内容

在 5 个维度上评分（0-5 整数，极其严格）：

**目标完成度**（Goal Achievement）：生成状态是否实现了文字描述的变化？
- 5：文字描述的变化完全、毫不模糊地实现。文字中提到的所有关键元素都存在且正确转换。无歧义。
- 4：目标实现，仅有轻微的非关键遗漏或格式差异。核心变化清晰可见且符合文字描述，但在布局、文字格式或非核心元素上可能有细微差异。
- 3：目标大部分实现但关键细节模糊/部分缺失。主要意图可识别，但重要元素不清楚、部分实现或需推理才能确认匹配文字描述。
- 2：部分实现；仅可见预期变化的小部分。大多数预期转换缺失或错误，虽然某些元素与文字描述有松散关联。
- 1：勉强相关；变化与文字语义不符。可能有表面相似性，但文字描述的核心变化不存在。
- 0：完全失败；无相关变化或完全错误的变化。生成图像显示要么没有变化，要么变化完全与文字描述无关。

**交互逻辑**（Interaction/State Logic）：变化是否符合可信的 GUI 交互和状态转换？
- 5：转换完全可信且符合标准 UI 行为。变化遵循自然的 GUI 交互模式，状态转换逻辑清晰，无不可能的跳跃或不连续。转换看起来像真实 UI 的行为。
- 4：大多可信；有轻微的不可信但仍可接受。整体转换有意义，但可能存在细微不一致，不破坏交互的可信度。
- 3：有某些不可信元素；仍部分连贯。变化在某些部分显示可识别的 UI 逻辑，但包含不遵循标准交互模式的元素。
- 2：大多不可信；状态转换破碎或 UI 行为不一致。变化显示重大逻辑问题。
- 1：几乎完全不合逻辑；UI 变化违反基本交互模式。转换违反基本 UI 原则。
- 0：不可能；严重的"传送"或无意义转换。

**一致性**（Preservation）：初始图像中不相关的区域是否保留？
- 5：未受影响的区域保留近乎完美。初始与生成图像的直接受影响区域外的每个像素都相同。
- 4：轻微漂移（小移位、轻微色彩/模糊变化）但清晰保留。
- 3：多个区域明显漂移，但整体 UI 身份保持。
- 2：目标区域外有显著意外变化。
- 1：广泛的意外变化；大部分 UI 被修改。
- 0：整个屏幕损坏或替换。

**UI 完整性**（UI Plausibility/Integrity）：UI 元素是否可信（无幻觉、无破碎布局）？
- 5：UI 组件连贯、结构正确、看起来原生。所有元素遵循平台约定。
- 4：大多连贯；轻微布局/元素问题。
- 3：多个元素/布局问题但仍类似可用 UI。
- 2：许多幻觉或严重布局问题。
- 1：UI 大多破碎；元素无意义。
- 0：UI 不可用或完全幻觉。

**视觉质量**（Visual Quality）：视觉可读性（文字/图标清晰度、伪影）。
- 5：清晰、易读、无明显伪影。
- 4：非常易读；轻微模糊/伪影。
- 3：易读但重要区域明显模糊/伪影。
- 2：显著质量下降；文字/图标难以阅读。
- 1：严重伪影；大部分文字不可读。
- 0：图像质量完全不可用。

基本规则：
- 仅基于视觉证据和提供的文字描述进行判断
- 勿猜测或假设图像中不可见的细节
- 对高分（4-5）极其保守（需铁证）
- 论证简洁（≤2 句）并引用具体观察
- 如不确定，请给予较低分数

仅输出 JSON：
{
  "goal": {"s": <0-5>, "j": "<论证>"},
  "logic": {"s": <0-5>, "j": "<论证>"},
  "consistency": {"s": <0-5>, "j": "<论证>"},
  "ui": {"s": <0-5>, "j": "<论证>"},
  "quality": {"s": <0-5>, "j": "<论证>"}
}
"""


TYPE2_EVAL_PROMPT_ZH = """你是一位 GUI 轨迹评估专家。评估一个 6 帧 UI 轨迹序列。

你将收到：
- 第 0 帧：初始状态（参考）
- 第 1-5 帧：显示任务进度的生成序列

在 5 个维度上评估（0-5）：

**任务完成度**：第 5 帧是否显示陈述目标的实现？
**交互逻辑**：帧间转换是否逻辑清晰和连贯？
**视觉一致性**：UI 元素在帧间是否保持稳定（无抖动、损坏）？
**元素完整性**：UI 元素是否看起来原生（无幻觉、无不可能状态）？
**视觉质量**：图像是否清晰（文字易读性好、伪影少）？

评分标准：5=完美，4=轻微问题，3=中等问题，2=显著问题，1=严重问题，0=完全失败

仅输出 JSON：
{
  "task_completion": {"s": <0-5>, "j": "<简洁论证>"},
  "interaction_logic": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_consistency": {"s": <0-5>, "j": "<简洁论证>"},
  "element_integrity": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_quality": {"s": <0-5>, "j": "<简洁论证>"}
}
"""


TYPE3_EVAL_PROMPT_ZH = """你是虚拟应用轨迹评估专家。

评估基于以下内容的多帧 UI 轨迹序列：
- 指令：用户的自然语言指令/目标
- 生成的帧：模型预测的 UI 演进

在 5 个维度上评估（0-5）：

**轨迹文字对齐度**：序列是否遵循指令轨迹？
**交互逻辑**：帧间转换是否逻辑清晰和连贯？
**视觉一致性**：UI 元素在帧间是否保持稳定？
**元素完整性**：UI 元素是否看起来原生（无幻觉）？
**视觉质量**：图像是否清晰且文字易读？

评分标准：5=完美，4=轻微问题，3=中等，2=显著问题，1=严重，0=完全失败

仅输出 JSON：
{
  "trajectory_text_alignment": {"s": <0-5>, "j": "<简洁论证>"},
  "interaction_logic": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_consistency": {"s": <0-5>, "j": "<简洁论证>"},
  "element_integrity": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_quality": {"s": <0-5>, "j": "<简洁论证>"}
}
"""


TYPE4_EVAL_PROMPT_ZH = """你是真实应用轨迹评估专家。

评估显示真实应用交互的多帧 UI 轨迹序列：
- 指令：用户的自然语言指令/目标
- 生成的帧：模型对真实应用的 UI 演进预测

在 5 个维度上评估（0-5）：

**轨迹文字对齐度**：序列是否遵循指令轨迹？
**交互逻辑**：帧间转换是否逻辑清晰和连贯？
**视觉一致性**：UI 元素在帧间是否保持稳定？
**元素完整性**：UI 元素是否看起来原生（无幻觉）？
**视觉质量**：图像是否清晰且文字易读？

评分标准：5=完美，4=轻微问题，3=中等，2=显著问题，1=严重，0=完全失败

仅输出 JSON：
{
  "trajectory_text_alignment": {"s": <0-5>, "j": "<简洁论证>"},
  "interaction_logic": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_consistency": {"s": <0-5>, "j": "<简洁论证>"},
  "element_integrity": {"s": <0-5>, "j": "<简洁论证>"},
  "visual_quality": {"s": <0-5>, "j": "<简洁论证>"}
}
"""


TYPE5_EVAL_PROMPT_ZH = """你是位置感知/空间任务评估专家。

评估生成的 UI 是否正确实现了指令中指定的位置感知任务。

维度：
- **位置准确性**：指令中的空间参考是否被正确表示？
- **交互逻辑**：UI 是否显示指定任务的逻辑状态？
- **元素完整性**：UI 元素是否可信且原生？
- **视觉质量**：图像是否清晰且易读？
- **指令遵循度**：整体输出是否匹配给定指令？

每个维度：0-5 分值

仅输出 JSON：
{
  "location_accuracy": {"s": <0-5>, "j": "<论证>"},
  "interaction_logic": {"s": <0-5>, "j": "<论证>"},
  "element_integrity": {"s": <0-5>, "j": "<论证>"},
  "visual_quality": {"s": <0-5>, "j": "<论证>"},
  "instruction_adherence": {"s": <0-5>, "j": "<论证>"}
}
"""


# ==================== PROMPT SELECTION UTILITIES ====================

def get_eval_prompt(data_type: str, lang_device: str = "english_phone") -> str:
    """
    Get appropriate evaluation prompt based on data type and language.

    Args:
        data_type: Type identifier ('type1', 'type2', 'type3', 'type4', 'type5')
        lang_device: Language/device identifier (e.g., 'chinese_phone', 'english_computer')

    Returns:
        Appropriate prompt string in the specified language
    """
    is_chinese = lang_device.startswith("chinese_")

    if data_type == "type1":
        return TYPE1_EVAL_PROMPT_ZH if is_chinese else TYPE1_EVAL_PROMPT
    elif data_type == "type2":
        return TYPE2_EVAL_PROMPT_ZH if is_chinese else TYPE2_EVAL_PROMPT
    elif data_type == "type3":
        return TYPE3_EVAL_PROMPT_ZH if is_chinese else TYPE3_EVAL_PROMPT
    elif data_type == "type4":
        return TYPE4_EVAL_PROMPT_ZH if is_chinese else TYPE4_EVAL_PROMPT
    elif data_type == "type5":
        return TYPE5_EVAL_PROMPT_ZH if is_chinese else TYPE5_EVAL_PROMPT
    else:
        raise ValueError(f"Unknown data type: {data_type}")
