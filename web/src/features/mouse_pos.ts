import React from "react";

const useMousePosition = () => {
    const [
        mousePosition,
        setMousePosition
    ] = React.useState({ x: 0, y: 0 });
    React.useEffect(() => {
        const updateMousePosition = (ev:React.MouseEvent) => {
            setMousePosition({ x: ev.clientX, y: ev.clientY });
        };
        // @ts-ignore
        window.addEventListener('mousemove', updateMousePosition);
        return () => {
            // @ts-ignore
            window.removeEventListener('mousemove', updateMousePosition);
        };
    }, []);
    return mousePosition;
};

export default useMousePosition;