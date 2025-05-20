import React from 'react';

export function Card({ title, children }) {
    return (
        <div className="bg-white shadow-md rounded-2xl p-6">
            {title && <h3 className="text-xl font-semibold mb-4">{title}</h3>}
            {children}
        </div>
    );
}

export function CardContent({ children }) {
    return <div className="text-gray-700">{children}</div>;
}
