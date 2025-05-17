document.getElementById("start").addEventListener("click", () => {
  fetch("http://localhost:5000")
    .then(() => alert("✅ Focus Guardian Started!"))
    .catch(() => alert("❌ Could not reach the Python server."));
});

document.getElementById("stop").addEventListener("click", () => {
  fetch("http://localhost:5000")
    .then(() => alert("🛑 Focus Guardian Stopped!"))
    .catch(() => alert("❌ Could not reach the Python server."));
});
