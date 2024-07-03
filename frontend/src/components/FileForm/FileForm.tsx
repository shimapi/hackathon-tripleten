import React, { ChangeEvent } from "react";
import "./FileForm.scss";

const FileForm: React.FC = () => {
	const handleFileUpload = (event: ChangeEvent<HTMLInputElement>) => {
		const file = event.target.files?.[0];
		if (file) {
			const reader = new FileReader();
			reader.onload = function (e: ProgressEvent<FileReader>) {
				if (e.target && typeof e.target.result === "string") {
					const data = JSON.parse(e.target.result);
					renderChart(data);
				}
			};
			reader.readAsText(file);
		}
	};

	const handleButtonClick = () => {
		const fileInput = document.getElementById("fileInput") as HTMLInputElement;
		const event = new Event("change", { bubbles: true });
		fileInput.dispatchEvent(event);
	};

	return (
		<div className="file">
			<section id="upload-section" className="file__form">
				<h2>Cargar Datos</h2>
				<input
					type="file"
					id="fileInput"
					accept=".json"
					onChange={handleFileUpload}
				/>
				<button id="loadDataButton" onClick={handleButtonClick}>
					Cargar Datos
				</button>
			</section>
		</div>
	);
};

// Define the type for your data if you know the structure
interface ChartData {
	// Add your data structure here
	[key: string]: string;
}

const renderChart = (data: ChartData) => {
	// Aquí iría tu lógica para renderizar el gráfico con los datos proporcionados
	console.log(data);
	// Ejemplo: Si estás utilizando Chart.js o D3.js, agregarías tu lógica aquí
};

export default FileForm;
