import { useDispatch, useSelector } from 'react-redux';
import { addAlert, removeAlert, clearAlerts } from '../store/slices/alertsSlice';
import { v4 as uuidv4 } from 'uuid';

export const useAlerts = () => {
    const dispatch = useDispatch();
    
    const showAlert = (message, type) => {
        const id = uuidv4();
        dispatch(addAlert({ id, message, type }));

        setTimeout(() => {
            closeAlert(id);
        }, 5000);
    };

    const closeAlert = (id) => {
        dispatch(removeAlert(id));
    };

    const clearAllAlerts = () => {
        dispatch(clearAlerts());
    };
    

    return {
        showAlert,
        closeAlert,
        clearAllAlerts,
    };
}