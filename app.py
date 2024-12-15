from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    {
        "question": "Python'da hangi anahtar kelime, bir döngüden çıkmak için kullanılır?",
        "options": [
            "exit",
            "break",
            "stop",
            "continue"
        ],
        "answer": "break"
    },
    {
        "question": "Python'da bir fonksiyon tanımlarken hangi anahtar kelime kullanılır?",
        "options": [
            "func",
            "define",
            "def",
            "function"
        ],
        "answer": "def"
    },
    {
        "question": "Aşağıdaki hangi ifade Python'da bir liste(array) oluşturur?",
        "options": [
            "list = (1, 2, 3)",
            "list = {1, 2, 3}",
            "list = [1, 2, 3]",
            "list = <1, 2, 3>"
        ],
        "answer": "list = [1, 2, 3]"
    },
    {
        "question": "Python'da hangi anahtar kelime bir istisnayı yakalamak için kullanılır?",
        "options": [
            "try",
            "catch",
            "except",
            "handle"
        ],
        "answer": "except"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(3):\n    print(i)\nelse:\n    print('Bitti')\n</code></pre>",
        "options": [
            "0 1 2",
            "0 1 2 Bitti",
            "Bitti",
            "Hata alır"
        ],
        "answer": "0 1 2 Bitti"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">x = '123'\ny = int(x) + 10\nz = str(y) + '45'\nprint(z)\n</code></pre>",
        "options": [
            "13345",
            "1345",
            "12345",
            "Hata alır"
        ],
        "answer": "13345"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(5):\n    if i == 3:\n        break\n    print(i, end=' ')\n</code></pre>",
        "options": [
            "0 1 2",
            "0 1 2 3",
            "0 1 2 3 4",
            "Hata alır"
        ],
        "answer": "0 1 2"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(5):\n    if i == 2:\n        continue\n    print(i, end=' ')\n</code></pre>",
        "options": [
            "0 1 3 4",
            "0 1 2 3 4",
            "0 1 2",
            "Hata alır"
        ],
        "answer": "0 1 3 4"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(1, 10, 2):\n    print(i, end=' ')\n</code></pre>",
        "options": [
            "1 2 3 4 5 6 7 8 9",
            "1 3 5 7 9",
            "0 2 4 6 8",
            "Hata alır"
        ],
        "answer": "1 3 5 7 9"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">def check(num):\n    if num % 2 == 0:\n        return True\n    return False\n\nprint(check(3))\n</code></pre>",
        "options": [
            "True",
            "False",
            "Hata alır",
            "0"
        ],
        "answer": "False"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(3):\n    print(i)\nelse:\n    print('Bitti')\n</code></pre>",
        "options": [
            "0 1 2",
            "0 1 2 Bitti",
            "Bitti",
            "Hata alır"
        ],
        "answer": "0 1 2 Bitti"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">def func(x):\n    return x + 1\n\nprint(func(5) * 2)\n</code></pre>",
        "options": [
            "6",
            "10",
            "11",
            "Hata alır"
        ],
        "answer": "10"
    },
    {
        "question": "Aşağıdaki kodda hangi hata vardır?\n\n<pre><code class=\"language-python\">x = [1, 2, 3]\nprint(x[3])\n</code></pre>",
        "options": [
            "IndexError",
            "ValueError",
            "TypeError",
            "Hata yok"
        ],
        "answer": "IndexError"
    },
    {
        "question": "Kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">my_list = [1, 2, 3]\nfor i in my_list:\n    my_list.remove(i)\nprint(my_list)\n</code></pre>",
        "options": [
            "[2]",
            "[1, 2, 3]",
            "[1, 3]",
            "Hata alır"
        ],
        "answer": "[1, 3]"
    },
    {
        "question": "Aşağıdaki kod parçasında hangi ifade doğrudur?\n\n<pre><code class=\"language-python\">x = '10'\ny = 5\nz = x + y\n</code></pre>",
        "options": [
            "z = 15",
            "z = '105'",
            "Hata alır",
            "z = 5.0"
        ],
        "answer": "Hata alır"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">for i in range(1, 10, 2):\n    print(i, end=' ')\n</code></pre>",
        "options": [
            "1 2 3 4 5 6 7 8 9",
            "1 3 5 7 9",
            "0 2 4 6 8",
            "Hata alır"
        ],
        "answer": "1 3 5 7 9"
    },
    {
        "question": "Aşağıdaki kodda hangi sonuç elde edilir?\n\n<pre><code class=\"language-python\">x = 'hello'\nprint(x[1:4])\n</code></pre>",
        "options": [
            "'hel'",
            "'llo'",
            "'ell'",
            "Hata alır"
        ],
        "answer": "'ell'"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">def check(num):\n    if num % 2 == 0:\n        return True\n    return False\n\nprint(check(3))\n</code></pre>",
        "options": [
            "True",
            "False",
            "Hata alır",
            "0"
        ],
        "answer": "False"
    },
    {
        "question": "Aşağıdaki kodun çıktısı nedir?\n\n<pre><code class=\"language-python\">a = [1, 2, 3]\nb = a.copy()\nb.append(4)\nprint(b, a)\n</code></pre>",
        "options": [
            "[1, 2, 3, 4] [1, 2, 3]",
            "[1, 2, 3] [1, 2, 3, 4]",
            "[1, 2, 3, 4] [1, 2, 3, 4]",
            "Hata alır"
        ],
        "answer": "[1, 2, 3, 4] [1, 2, 3]"
    },
    {
        "question": "Aşağıdaki kodda hangi işlem doğrudur?\n\n<pre><code class=\"language-python\">x = (1, 2, 3)\nx[0] = 4\n</code></pre>",
        "options": [
            "Değişiklik yapılabilir",
            "Hata alır",
            "Değişiklik yapılabilir, ama gereksiz",
            "Hata yoktur"
        ],
        "answer": "Hata alır"
    }
]

@app.route('/')
def index():
    response = redirect(url_for('quiz', q=0))
    response.set_cookie('correct', '0')
    response.set_cookie('incorrect', '0')
    return response

@app.route('/quiz/<int:q>', methods=['GET', 'POST'])
def quiz(q):
    if request.method == 'POST':
        selected_option = request.form.get('option')
        if selected_option:
            if selected_option == questions[q]["answer"]:
                correct = int(request.cookies.get('correct', 0)) + 1
                response = redirect(url_for('quiz', q=q+1))
                response.set_cookie('correct', str(correct))
                response.set_cookie(f'question_{q}', 'correct')
            else:
                incorrect = int(request.cookies.get('incorrect', 0)) + 1
                response = redirect(url_for('quiz', q=q+1))
                response.set_cookie('incorrect', str(incorrect))
                response.set_cookie(f'question_{q}', 'incorrect')
            return response

    question = questions[q]
    return render_template('quiz.html', question=question, q=q, total=len(questions))

@app.route('/finish', methods=['POST'])
def finish():
    return redirect(url_for('result'))

@app.route('/result')
def result():
    correct = int(request.cookies.get('correct', 0))
    incorrect = int(request.cookies.get('incorrect', 0))
    results = []
    for i, question in enumerate(questions):
        status = request.cookies.get(f'question_{i}', 'unanswered')
        results.append({
            'question': question['question'],
            'correct_answer': question['answer'],
            'status': status
        })
    return render_template('result.html', correct=correct, incorrect=incorrect, results=results)

if __name__ == "__main__":
    app.run(debug=True)
