async function loadTopics() {
  const res = await fetch("data.json");
  const topics = await res.json();

  const container = document.getElementById("topics");

  container.innerHTML = `
    <p><strong>Last updated:</strong> ${new Date().toLocaleDateString("en-GB")}</p>
  ` + topics.map(topic => `
    <div class="card">
      <h2>${topic.name}</h2>
      <p>${topic.mentions} mentions this week</p>
      <p>${topic.trend === "up" ? "📈 Rising" : "📉 Falling"}</p>
    </div>
  `).join("");
}

loadTopics();
