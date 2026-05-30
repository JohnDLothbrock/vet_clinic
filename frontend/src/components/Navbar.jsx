import { Link } from "react-router-dom";

function Navbar() {

  return (

    <nav className="navbar">

      <Link to="/">
        Dashboard
      </Link>

      <Link to="/pets">
        Pets
      </Link>

      <Link to="/owners">
        Owners
      </Link>

      <Link to="/appointments">
        Appointments
      </Link>

    </nav>
  );
}

export default Navbar;