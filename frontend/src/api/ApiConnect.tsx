import { useEffect, useState } from "react";

const ApiConnect = () => {
	const [data, setData] = useState<{ id: number; title: string }[]>([]);

	useEffect(() => {
		async function fetchData() {
			console.log(import.meta.env.VITE_API_URL);
			try {
				const response = await fetch(`${import.meta.env.VITE_API_URL}/posts`);

				if (!response.ok) {
					throw new Error("Error en la peticion");
				}
				const data = await response.json();
				console.log(data);
				setData(data);
			} catch (error) {
				console.log("Error en la peticion", error);
			}
		}

		fetchData();
	}, []);

	return (
		<div>
			<h1>Api Connect</h1>
			<ul>
				{data.map((item) => (
					<li key={item.id}>{item.title}</li>
				))}
			</ul>
		</div>
	);
};

export default ApiConnect;
