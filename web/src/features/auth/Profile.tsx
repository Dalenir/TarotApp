import User from "../../interfaces/User";
import {Button, Container} from "react-bootstrap";
import './Profile.css';
import Board from "../board/Board";


 // TODO: ONLY FOR DEMOSTRATION PURPOSES, REDO ALL

interface ProfileProps {
    user: User | undefined,
    handle_logout: () => void
}

export default function Profile({ user, handle_logout } : ProfileProps) {

    return (
        <Container fluid className="align-items-center vh-100 d-flex justify-content-center">
            <Board />
            <div className='simple_username'>
                {user && <h1>Hello, {user.name}!</h1>}
                {user?.payer && <h2>Thank you for your support!</h2>}
                <Button variant="dark" onClick={handle_logout}>Logout</Button>
            </div>
        </Container>
    );
};