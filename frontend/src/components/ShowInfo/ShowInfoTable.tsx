import { useEffect, useState } from "react";

const ShowInfoTable = ({ filename }: { filename: string }) => {
	const [data, setData] = useState([]);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await fetch(`/json/${filename}`);
				if (!response.ok) {
					throw new Error("Network response was not ok");
				}
				const data = await response.json();
				setData(data);
			} catch (error) {
				console.error("Error fetching the data", error);
			}
		};

		fetchData();
	}, [filename]);

	return (
		<div>
			<h2>Data from {filename}</h2>
			{data.length > 0 ? (
				<table>
					<thead>
						<tr>
							{Object.keys(data[0]).map((key) => (
								<th key={key}>{key}</th>
							))}
						</tr>
					</thead>
					<tbody>
						{data.map((item, index) => (
							<tr key={index}>
								{Object.values(item).map((value, idx) => (
									<td key={idx}>{value as React.ReactNode}</td>
								))}
							</tr>
						))}
					</tbody>
				</table>
			) : (
				<p>No data available</p>
			)}
		</div>
	);
};

export default ShowInfoTable;
