import React, { useState } from "react";

const FileCsv: React.FC = () => {
	const [file, setFile] = useState<File | null>(null);

	const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
		if (event.target.files) {
			setFile(event.target.files[0]);
		}
	};

	const handleUpload = async () => {
		if (file) {
			const formData = new FormData();
			formData.append("file", file);

			try {
				const response = await fetch("/api/upload", {
					method: "POST",
					body: formData,
				});

				if (response.ok) {
					console.log("Archivo subido correctamente.");
				} else {
					console.error("Error al subir el archivo.");
				}
			} catch (error) {
				console.error("Error de red:", error);
			}
		}
	};

	return (
		<div>
			<input type="file" onChange={handleFileChange} />
			<button onClick={handleUpload}>Subir archivo</button>
		</div>
	);
};

export default FileCsv;
