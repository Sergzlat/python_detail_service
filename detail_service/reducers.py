from redux import combineReducers
from userSlice import userReducer
from detailLSlice import detailLReducer

rootReducer = combineReducers({
  'user': userReducer,
  'detailL': detailLReducer,
})

RootState = type(rootReducer)
export default rootReducer

import { combineReducers } from "redux";
import userReducer from "./userSlice";
import detailLReducer from "./detailLSlice";

const rootReducer = combineReducers({
  user: userReducer,
  detailL: detailLReducer,
});

export type RootState = ReturnType<typeof rootReducer>;

export default rootReducer;
