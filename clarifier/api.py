import google.generativeai as palm
import difflib


def highlight_diff(before, after):
    differ = difflib.Differ()
    diff = list(differ.compare(before.splitlines(), after.splitlines()))
    
    highlighted_code = []
    for line in diff:
        if line.startswith('  '):  # Unchanged line
            highlighted_code.append(line[2:])
        elif line.startswith('+ '):  # Added line
            highlighted_code.append(f"\033[92m{line[2:]}\033[0m")
    
    return '\n'.join(highlighted_code)

def get_new_code(code_file_path) -> str:
    palm.configure(api_key="AIzaSyD1O94WxFVfJCqRnKmFSnxD8Y7TXPvj2Qk")
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    file = open(code_file_path, "r")
    text = file.read()
    if len(text) < 25:
        return text, text
    file.close()


    prompt = "Add comments and/or docstrings to make the code more readable. The code is as follows: \n\n" + text

    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        max_output_tokens=800,
    )

    response = completion.result
    if completion.result == None:
        return text, text
    lines = response.split("\n")
    del lines[0]
    del lines[-1]
    response = "\n".join(lines)

    return text, response

