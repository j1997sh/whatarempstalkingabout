async function loadTopics() {
  const res = await fetch("data.json");
  const data = await res.json();

  const container = document.getElementById("topics");

  container.innerHTML = `
    <p><strong>Last updated:</strong> ${data.lastUpdated}</p>
  ` + data.topics.map(topic => `
    <div class="card">
      <h2>${topic.name}</h2>
      <p>${topic.mentions} Hansard search mentions</p>
      <p>${topic.trend === "up" ? "📈 Rising" : "📉 Falling"}</p>
    </div>
  `).join("");
}

loadTopics();
