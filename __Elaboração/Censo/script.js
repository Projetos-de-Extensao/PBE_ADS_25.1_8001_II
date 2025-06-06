let ultimoEnvio = null;

document.getElementById("censoForm").addEventListener("submit", function(event) {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(event.target).entries());
  console.log("🔍 Dados coletados:", data);
  alert("Formulário enviado com sucesso!");
  ultimoEnvio = data;
});

// Exportar para JSON
function exportToJSON() {
  if (!ultimoEnvio) {
    alert("Envie o formulário primeiro.");
    return;
  }

  const jsonString = JSON.stringify(ultimoEnvio, null, 2);
  const blob = new Blob([jsonString], { type: "application/json" });
  const link = document.createElement("a");

  link.href = URL.createObjectURL(blob);
  link.download = "censo-ilha-primeira.json";
  link.click();
}

// Exportar para CSV
function exportToCSV() {
  if (!ultimoEnvio) {
    alert("Envie o formulário primeiro.");
    return;
  }

  const headers = Object.keys(ultimoEnvio);
  const values = Object.values(ultimoEnvio);

  let csvContent = headers.join(",") + "\n" + values.map(escapeCSV).join(",");

  const blob = new Blob([csvContent], { type: "text/csv" });
  const link = document.createElement("a");

  link.href = URL.createObjectURL(blob);
  link.download = "censo-ilha-primeira.csv";
  link.click();
}

function escapeCSV(value) {
  if (typeof value === "string" && (value.includes(",") || value.includes('"'))) {
    return `"${value.replace(/"/g, '""')}"`;
  }
  return value;
}
