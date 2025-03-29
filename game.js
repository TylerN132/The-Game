let gameText = document.getElementById("game-text");
let choicesContainer = document.getElementById("choices");

function startGame() {
    document.getElementById("game-container").style.display = "block";
    document.querySelector(".start-button").style.display = "none";

    updateGame(
        `You awaken in a dark forest, a crisp brush of wind sends chills down your spine.<br>
        Your head aches as you feel something drip down. Dazed, you look around and notice a light on the ground.<br>
        <br><strong>What do you do?</strong>`,
        [
            { text: "Crawl to the light", next: "crawlToLight" },
            { text: "Check your head", next: "checkHead" },
            { text: "Yell for help", next: "yellForHelp" }
        ]
    );
}

function updateGame(storyText, choices) {
    document.getElementById("game-container").innerHTML = `
        <h2>Game Started!</h2>
        <p>${storyText}</p>
        <div id="choices" class="choice-container"></div>
    `;

    let choicesContainer = document.getElementById("choices");

    choices.forEach(choice => {
        let button = document.createElement("button");
        button.innerHTML = choice.text;
        button.classList.add("choice-button");
        button.onclick = () => makeChoice(choice.next);
        choicesContainer.appendChild(button);
    });
}

function makeChoice(choice) {
    switch (choice) {
        case "crawlToLight":
            updateGame(
                `You slowly crawl towards the mysterious light, unsure of what lies ahead.<br>
                You find a flashlight on the ground and pick it up, revealing a corpse next to you and an overturned vehicle.<br>
                <br><strong>What do you do next?</strong>`,
                [
                    { text: "Check the corpse", next: "checkCorpse" },
                    { text: "Check the vehicle", next: "checkVehicle" },
                    { text: "Begin walking into the woods", next: "walkWoods" }
                ]
            );
            break;
        case "checkHead":
            updateGame("You touch your head and feel a warm, sticky substance. It's blood.<br> You feel dizzy and collapse... <strong>GAME OVER.</strong>", []);
            break;
        case "yellForHelp":
            updateGame("You yell for help, but your voice fades into the silence of the forest.<br> The darkness grows around you... <strong>GAME OVER.</strong>", []);
            break;
        case "checkCorpse":
            updateGame(
                `You roll the corpse over to reveal a face half torn apart.<br>
                The part of the face you can see is familiar, but you cannot recall who it is.<br>
                In the corpse's pants is a wallet with a picture of the two of you.`,
                []
            );
            break;
        case "checkVehicle":
            updateGame(
                `You walk over to the overturned vehicle and notice it is a 1964 Mustang.<br>
                You shine the light inside and begin looking for anything useful.<br>
                You open the glove compartment and find a half-empty bottle of whiskey and some camping equipment in the back seat.`,
                []
            );
            break;
        case "walkWoods":
            updateGame("You feel like you should go back and check the corpse and the car first.", []);
            break;
        default:
            updateGame("Something went wrong!", []);
    }
}
