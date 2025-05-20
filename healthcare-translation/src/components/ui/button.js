export function Button({ children, onClick, variant = 'primary', disabled = false }) {
    const baseStyles = 'px-4 py-2 rounded-xl text-sm font-medium focus:outline-none';
    const variants = {
        primary: 'bg-blue-500 text-white hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed',
        secondary: 'bg-gray-200 text-gray-700 hover:bg-gray-300 disabled:opacity-50 disabled:cursor-not-allowed',
        danger: 'bg-red-500 text-white hover:bg-red-600 disabled:opacity-50 disabled:cursor-not-allowed',
    };

    return (
        <button
            onClick={!disabled ? onClick : null}
            className={`${baseStyles} ${variants[variant] || variants.primary}`}
            disabled={disabled}
        >
            {children}
        </button>
    );
}
