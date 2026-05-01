const topics = [
  { name: "NHS", mentions: 42 },
  { name: "Housing", mentions: 31 },
  { name: "Immigration", mentions: 28 },
  { name: "Economy", mentions: 23 },
  { name: "Climate", mentions: 12 }
];

const container = document.getElementById("topics");

container.innerHTML = topics.map(topic => `
  <div class="card">
    <h2>${topic.name}</h2>
    <p>${topic.mentions} mentions this week</p>
  </div>
`).join("");
