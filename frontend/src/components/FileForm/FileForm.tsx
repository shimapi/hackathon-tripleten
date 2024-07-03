import React from "react";
import "./FileForm.scss";
// import { useHistory, useLocation, useParams, useRouteMatch } from 'react-router-dom';

// Si necesitas definir parámetros para useParams, puedes hacerlo aquí.
// Por ejemplo, si esperas un parámetro "id" en la ruta, puedes definirlo así:
// interface RouteParams {
//   id: string;
// }

const FileForm: React.FC = () => {
	// Aquí es donde usarías los hooks, si necesitas acceder a las props del router.
	// const history = useHistory();
	// const location = useLocation();
	// const params = useParams<RouteParams>();
	// const match = useRouteMatch();

	return (
		<div className="file">
			<form
				action="/upload"
				method="post"
				encType="multipart/form-data"
				className="file__form"
			>
				<input type="file" name="file" />
				<button type="submit">Subir</button>
			</form>
		</div>
	);
};

export default FileForm;
