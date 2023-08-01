from typing import Union
from fastapi import FastAPI , HTTPException
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from fastlid import fastlid, supported_langs
from lib import *

def translate( input , target_lang ):
    #set predict lang
    fastlid.set_languages = supported_langs
    translation_pipeline = pipeline('translation',
                                    model = model,
                                    tokenizer = tokenizer,
                                    src_lang = fastlid(input)[0],
                                    tgt_lang = target_lang,
                                    max_length = 400,
                                    device=0)
    return translation_pipeline(input)[0]['translation_text']

app = FastAPI()

@app.get("/items/")
async def get_info(input: Union[str, None] = None,target_lang: Union[str, None] = None):
    if not input : 
        return Errors.UNSUPPORTED_INPUT_FORMAT
    if target_lang not in language :
        return Errors.UNSUPPORTED_LANGUAGE_ERROR
    
    results = translate(input,target_lang)
    torch.cuda.empty_cache()
    return {"result": results}

if __name__ == '__main__' : 
    import uvicorn
    uvicorn.run(app , host = "0.0.0.0" , port=9321)