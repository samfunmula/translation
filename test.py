from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import fasttext
from fastlid import fastlid, supported_langs


checkpoint = 'facebook/nllb-200-distilled-600M'

model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

def translate( input , target_lang ):
    #set predict lang
    fastlid.set_languages = supported_langs
    translation_pipeline = pipeline('translation',
                                    model = model,
                                    tokenizer = tokenizer,
                                    src_lang = fastlid(input)[0],
                                    tgt_lang = target_lang,
                                    max_length = 400)
    return translation_pipeline(input)[0]['translation_text']

input = 'これはテストですが、一度だけ表示されます'
target_lang = 'eng_Latn'

output=translate(input,target_lang)
print(output)


