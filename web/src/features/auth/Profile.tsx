import User from "../../interfaces/User";
import {Button} from "react-bootstrap";

interface ProfileProps {
    user: User | undefined,
    handle_logout: () => void
}

export default function Profile({ user, handle_logout } : ProfileProps) {

    console.log('profile level', user)

    return (
        <>
            {user && <h1>{user.name} profile page</h1>}
            {user?.payer && <h2>Thank you for your support!</h2>}
            <Button variant="dark" onClick={handle_logout}>Logout</Button>

        </>
    );
};