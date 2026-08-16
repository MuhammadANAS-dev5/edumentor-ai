function showTutor() {

    document.getElementById("workspace").innerHTML = `
        <h2>AI Tutor</h2>

        <div id="chat-box" class="chat-box">

            <div class="message ai-message">
                Hello! I'm EduMentor AI.
                What would you like to learn?
            </div>

        </div>

        <div class="input-area">

            <input
                type="text"
                id="question"
                placeholder="Ask your question..."
            >

            <button onclick="askQuestion()">
                Ask
            </button>

        </div>
    `;
}


function askQuestion() {

    const input =
        document.getElementById("question");

    const question =
        input.value.trim();

    if (!question) {
        return;
    }

    const chat =
        document.getElementById("chat-box");

    chat.innerHTML += `
        <div class="message user-message">
            ${question}
        </div>
    `;

    input.value = "";

    chat.innerHTML += `
        <div class="message ai-message">
            AI response will appear here.
        </div>
    `;

    chat.scrollTop = chat.scrollHeight;
}


function showQuiz() {

    document.getElementById("workspace").innerHTML = `
        <h2>AI Quiz</h2>

        <p>
            Generate an AI-powered quiz
            based on your selected topic.
        </p>
    `;
}


function showPerformance() {

    document.getElementById("workspace").innerHTML = `
        <h2>My Performance</h2>

        <p>
            Your learning performance
            will appear here.
        </p>
    `;
}


function showStudyPlan() {

    document.getElementById("workspace").innerHTML = `
        <h2>Personalized Study Plan</h2>

        <p>
            Your AI-generated study plan
            will appear here.
        </p>
    `;
}