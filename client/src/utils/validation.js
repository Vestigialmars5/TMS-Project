export const validators = {
    email: (value) => {
        // Email is required
        // Email address is invalid
        if (!value) return "Email Is Required";
        if (!/\S+@\S+\.\S+/.test(value)) return "Email Address Is Invalid";
        return "";
    },
    password: (value) => {
        // Password is required
        // Password must be at least 8 characters
        // Password must be at most 14 characters
        if (!value) return "Password Is Required";
        if (value.length < 8) return "Password Must Be At Least 8 Characters";
        if (value.length > 14) return "Password Must Be At Most 14 Characters";
        return "";
    },
    name: (value) => {
        // Name is required
        // Name must be at least 2 characters
        // Name must not be more than 30 characters
        // Name must not contain any numbers
        // Name must not contain any special characters
        if (!value) return "Name Is Required";
        if (value.length < 2) return "Name Must Be At Least 2 Characters";
        if (value.length > 50) return "Name Must Not Be More Than 30 Characters";
        if (/\d/.test(value)) return "Name Must Not Contain Any Numbers";
        if (/[!@#$%^&*(),.?":{}|<>]/.test(value)) return "Name Must Not Contain Any Special Characters";
        return "";
    },
    address: (value) => {
        // Address is required
        // Address must be at least 10 characters
        // Address must not be more than 50 characters
        if (!value) return "Address Is Required";
        if (value.length < 10) return "Address Must Be At Least 10 Characters";
        if (value.length > 50) return "Address Must Not Be More Than 50 Characters";
        return "";
    },
    phoneNumber: (value) => {
        // Phone number is required
        // Phone number must be 10 digits
        // Phone number must not contain any characters
        if (!value) return "Phone Number Is Required";
        if (value.length !== 10) return "Phone Number Must Be 10 Digits";
        if (/\D/.test(value)) return "Phone Number Must Not Contain Any Characters";
        return "";
    },
    companyName: (value) => {
        // Company name is required
        // Company name must be at least 2 characters
        // Company name must not be more than 30 characters
        // Company name must not contain any special characters
        if (!value) return "Company Name Is Required";
        if (value.length < 2) return "Company Name Must Be At Least 2 Characters";
        if (value.length > 50) return "Company Name Must Not Be More Than 30 Characters";
        if (/[!@#$%^&*(),.?":{}|<>]/.test(value)) return "Company Name Must Not Contain Any Special Characters";
        return "";
    },
    id: (value) => {
        // ID is required
        // ID must be an integer
        if (!value) return "ID Is Required";
        if (!Number.isInteger(Number(value))) return "ID Must Be An Integer";
    },
}