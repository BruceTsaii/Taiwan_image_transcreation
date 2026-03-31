import json
import random
import re

class TaiwanTranscreator:
    def __init__(self, concept_file='data/taiwan_concepts.json'):
        """
        初始化：讀取台灣文化概念資料庫
        """
        try:
            with open(concept_file, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            # Fallback data if file not found (for demonstration)
            self.data = {
                "categories": {
                    "food_and_drink": [{"concept": "Bubble Tea", "keywords": ["boba tea", "pearl milk tea"]}],
                    "transportation": [{"concept": "Scooters", "keywords": ["scooters", "mopeds", "helmets"]}],
                    "architecture_and_street": [{"concept": "Temple", "keywords": ["ornate temple", "red pillars"]}]
                }
            }
            print("Warning: concept file not found, using fallback data.")

    def analyze_intent(self, prompt):
        """
        簡單的意圖分析，判斷 Prompt 屬於哪個類別
        (在實際專案中，這裡會是 LLM 的工作)
        """
        prompt_lower = prompt.lower()
        if any(w in prompt_lower for w in ['eat', 'food', 'drink', 'lunch', 'dinner', 'snack']):
            return 'food_and_drink'
        elif any(w in prompt_lower for w in ['street', 'road', 'car', 'drive', 'traffic', 'travel']):
            return 'transportation'
        elif any(w in prompt_lower for w in ['house', 'building', 'home', 'shop', 'store']):
            return 'architecture_and_street'
        elif any(w in prompt_lower for w in ['celebrate', 'party', 'festival', 'new year']):
            return 'festivals_and_customs'
        return 'random' # 預設

    def transcreate(self, original_prompt, strict_mode=False):
        """
        將原始 Prompt 轉譯為台灣語境 Prompt
        """
        category_key = self.analyze_intent(original_prompt)
        
        # 如果是 Random，則從所有類別中隨機選一個來豐富畫面
        if category_key == 'random':
            all_cats = list(self.data['categories'].keys())
            category_key = random.choice(all_cats)
        
        concepts = self.data['categories'].get(category_key, [])
        if not concepts:
            return f"Taiwanese style photo of {original_prompt}"

        # 隨機選取一個該類別的台灣概念
        selected_concept = random.choice(concepts)
        concept_keywords = ", ".join(selected_concept['keywords'])
        
        # 構建新的 Prompt (模擬 LLM 的輸出)
        # 結構: [台灣環境氛圍] + [核心動作替換] + [細節增強]
        
        transcreated_prompt = ""
        
        # 這裡模擬論文中的編輯邏輯：替換主體或增加背景
        if category_key == 'food_and_drink':
            transcreated_prompt = f"A photo taken in Taiwan. {original_prompt}, featuring {concept_keywords} on the table. Authentic Taiwanese street food vibe, high resolution."
        
        elif category_key == 'transportation':
            transcreated_prompt = f"A photo of a street in Taiwan. {original_prompt}. Background filled with {concept_keywords} and traditional vertical signboards. Cinematic lighting."
            
        elif category_key == 'architecture_and_street':
             transcreated_prompt = f"Taiwanese street photography. {original_prompt}. Featuring {concept_keywords}. Urban, realistic texture."
             
        else:
             transcreated_prompt = f"A photo in Taiwan context. {original_prompt}. Including elements like {concept_keywords}. 4k quality."

        return {
            "original": original_prompt,
            "category_detected": category_key,
            "concept_injected": selected_concept['concept'],
            "transcreated_prompt": transcreated_prompt
        }

# 測試用
if __name__ == "__main__":
    transcreator = TaiwanTranscreator()
    
    test_prompts = [
        "A family eating dinner together.",
        "A busy city street during rush hour.",
        "An old building with plants."
    ]
    
    print("--- Taiwan Image Transcreation Simulation ---\n")
    for p in test_prompts:
        result = transcreator.transcreate(p)
        print(f"Input: {result['original']}")
        print(f"Concept: {result['concept_injected']}")
        print(f"Output Prompt: {result['transcreated_prompt']}\n")